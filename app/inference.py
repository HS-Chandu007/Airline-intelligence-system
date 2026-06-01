from app.model_loader import sentiment_model, reason_model


SENTIMENT_MAP = {
    0: "negative",
    1: "neutral",
    2: "positive"
}


class InferencePipeline:

    def predict(self, df):

        sentiment_pred = sentiment_model.predict(df)[0]

        sentiment = SENTIMENT_MAP[sentiment_pred]

        reason = None

        if sentiment == "negative":
            reason = reason_model.predict(df)[0]

        return {
            "sentiment": sentiment,
            "reason": reason
        }