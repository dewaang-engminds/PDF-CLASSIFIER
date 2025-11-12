import re
from collections import Counter
from typing import Dict, List


def tokenize(text: str) -> Counter:
    """
    Tokenize text into lowercase alphanumeric tokens and return Counter.
    """
    tokens = re.findall(r"\b[a-zA-Z0-9%.-]+\b", text.lower())
    return Counter(tokens)


def count_phrase_occurrences(text: str, phrase: str) -> int:
    """
    Count non-overlapping occurrences of a phrase in text.
    """
    pattern = re.compile(r"\b" + re.escape(phrase.lower()) + r"\b")
    return len(pattern.findall(text.lower()))


def batch_count_phrases(text: str, phrases: List[str]) -> Dict[str, int]:
    """
    Count all phrases efficiently and return dict {phrase: count}.
    """
    results = {}
    text_lower = text.lower()
    for p in phrases:
        pattern = re.compile(r"\b" + re.escape(p.lower()) + r"\b")
        results[p.lower()] = len(pattern.findall(text_lower))
    return results