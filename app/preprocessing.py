import re
import pandas as pd


def clean_text(text: str) -> str:
    """
    Clean raw tweet text.
    """

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"@\w+", "", text)

    text = re.sub(r"#", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def create_features(text: str) -> dict:
    """
    Generate engineered text features.
    """

    cleaned = clean_text(text)

    words = cleaned.split()

    word_count = len(words)

    avg_word_length = (
        sum(len(word) for word in words) / word_count
        if word_count > 0 else 0
    )

    return {
        "clean_text": cleaned,
        "word_count": word_count,
        "avg_word_length": avg_word_length
    }


def prepare_dataframe(text: str, airline: str) -> pd.DataFrame:
    """
    Convert raw API input into model-ready dataframe.
    """

    features = create_features(text)

    data = pd.DataFrame([{
        "clean_text": features["clean_text"],
        "airline": airline,
        "word_count": features["word_count"],
        "avg_word_length": features["avg_word_length"]
    }])

    return data