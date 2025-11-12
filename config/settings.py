from pathlib import Path
import yaml


DEFAULT_CONFIG_PATH = Path(__file__).parent / "env.yaml"


def load_config(path: str = None) -> dict:
    """Load and validate YAML configuration."""
    cfg_path = Path(path) if path else DEFAULT_CONFIG_PATH
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")

    with open(cfg_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # --- Validation ---
    if not isinstance(cfg, dict):
        raise ValueError("Invalid config format: must be a YAML mapping.")

    # Threshold
    threshold = cfg.get("THRESHOLD", 0.6)
    if not isinstance(threshold, (float, int)) or threshold <= 0.5:
        raise ValueError("THRESHOLD must be a number greater than 0.5.")

    # Beta and Epsilon
    beta = cfg.get("BETA", 0.8)
    epsilon = cfg.get("EPSILON", 0.05)
    if not (0.0 <= beta <= 1.0):
        raise ValueError("BETA must be between 0.0 and 1.0.")
    if epsilon < 0.0:
        raise ValueError("EPSILON must be non-negative.")

    # Types
    types = cfg.get("TYPES")
    if not types or not isinstance(types, dict):
        raise ValueError("TYPES section missing or malformed in config.")

    for tname, details in types.items():
        if "keywords" not in details or not isinstance(details["keywords"], list):
            raise ValueError(f"{tname}: 'keywords' list required.")
        weights = details.get("weights", [])
        if weights and len(weights) != len(details["keywords"]):
            raise ValueError(f"{tname}: number of weights must match number of keywords.")

    # Storage
    storage = cfg.get("STORAGE", {})
    if not isinstance(storage, dict):
        raise ValueError("STORAGE section must be a dictionary.")

    return cfg