# Example for future use
from pydantic import BaseModel

class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    original: str
    summary: str
