from typing import Tuple, Dict, Any
from utils.text_utils import batch_count_phrases
from config.settings import load_config
import math


def classify_document(text: str, config_path: str = None) -> Tuple[str, Dict[str, float], Dict[str, Any]]:
    """
    Weighted, normalized, and coverage-based classification engine.
    Returns:
        final_type (str): predicted type or 'UNKNOWN'
        scores (dict): normalized scores per type
        details (dict): detailed per-type keyword breakdown
    """
    cfg = load_config(config_path)
    types_cfg = cfg["TYPES"]
    threshold = cfg.get("THRESHOLD", 0.6)
    beta = cfg.get("BETA", 0.8)
    epsilon = cfg.get("EPSILON", 0.05)

    text_lower = text.lower()
    total_tokens = max(len(text_lower.split()), 1)

    type_raw_scores = {}
    type_details = {}

    # Step 1: Compute weighted normalized freq per type
    for type_name, tinfo in types_cfg.items():
        keywords = tinfo.get("keywords", [])
        weights = tinfo.get("weights", [1.0] * len(keywords))

        # Count all keywords efficiently
        freq_map = batch_count_phrases(text_lower, keywords)
        keyword_details = []

        type_raw_score = 0.0
        appeared_keywords = 0

        for kw, w in zip(keywords, weights):
            k_lower = kw.lower()
            freq = freq_map.get(k_lower, 0)
            norm_freq = freq / total_tokens
            weighted = norm_freq * w
            type_raw_score += weighted
            if freq > 0:
                appeared_keywords += 1

            keyword_details.append({
                "keyword": kw,
                "frequency": freq,
                "weight": w,
                "normalized_freq": round(norm_freq, 6),
                "weighted_score": round(weighted, 6)
            })

        coverage = appeared_keywords / len(keywords) if keywords else 0.0
        type_details[type_name] = {
            "keywords": keyword_details,
            "type_raw_score": round(type_raw_score, 6),
            "coverage": round(coverage, 4)
        }
        type_raw_scores[type_name] = type_raw_score

    # Step 2: Normalize raw scores
    total_raw = sum(type_raw_scores.values())
    if total_raw == 0:
        return "UNKNOWN", {}, {"reason": "no keyword matches"}

    normalized = {t: (v / total_raw) for t, v in type_raw_scores.items()}

    # Step 3: Combine with coverage
    combined_scores = {}
    for t in normalized:
        presence = normalized[t]
        coverage = type_details[t]["coverage"]
        combined = beta * presence + (1 - beta) * coverage
        combined_scores[t] = combined
        type_details[t]["presence_score"] = round(presence, 6)
        type_details[t]["final_type_score"] = round(combined, 6)

    # Step 4: Apply threshold and tie logic
    best_type, best_score = max(combined_scores.items(), key=lambda x: x[1])
    sorted_scores = sorted(combined_scores.values(), reverse=True)
    second_best = sorted_scores[1] if len(sorted_scores) > 1 else 0.0

    if best_score < threshold:
        decision = "UNKNOWN"
        reason = f"best_score {best_score:.3f} below threshold {threshold}"
    elif abs(best_score - second_best) < epsilon:
        decision = "UNKNOWN"
        reason = f"tie within epsilon ({epsilon})"
    else:
        decision = best_type
        reason = f"matched {best_type} (score={best_score:.3f})"

    type_details["decision"] = {"chosen": decision, "reason": reason, "threshold": threshold}
    return decision, combined_scores, type_details