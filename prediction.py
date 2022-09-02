from pathlib import Path
from typing import Dict

import joblib

from preprocessor import TextCleaner
import gdown


def load_pipeline(model_path: Path):
    if not model_path.exists():
        gdown.download('https://drive.google.com/uc?export=download&id=1IjK8lMhIo2iqd85D7qo93plNXmliIAsU',
                       str(model_path),
                       quiet=False)
    return joblib.load(model_path)


text_cleaner = TextCleaner()
pipeline = load_pipeline(Path('classifier_pipeline.pkl'))


def predict(body: Dict):
    review_text = body.get('review', None)

    if not review_text:
        return {}

    return {'model_outputs': classify_review(review_text)}


def classify_review(review: str):
    cleaned_review = text_cleaner.transform([review])
    output_probs = pipeline.predict_proba(cleaned_review)
    return {'positive_proba': output_probs[0, 0],
            'negative_proba': output_probs[0, 1]}
