from pathlib import Path
import joblib


BASE_DIR = Path(__file__).resolve().parent

ARTIFACTS_DIR = BASE_DIR / "artifacts"


sentiment_model = joblib.load(
    ARTIFACTS_DIR / "sentiment_pipeline.pkl"
)

reason_model = joblib.load(
    ARTIFACTS_DIR / "reason_pipeline.pkl"
)

        
    