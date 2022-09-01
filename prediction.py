from typing import Dict

import joblib

from preprocessor import TextCleaner

text_cleaner = TextCleaner()
pipeline = joblib.load('classifier_pipeline.pkl')

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
