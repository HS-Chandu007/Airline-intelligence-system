from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(
        min_length=4,
        example="My flight got delayed for 5 hours"
    )

    airline: str = Field(
        ...,
        example="United"
    )


class PredictResponse(BaseModel):
    sentiment: str
    reason: str | None = None