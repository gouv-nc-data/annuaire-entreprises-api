from fastapi import APIRouter
from pydantic import BaseModel

from app.services.feedback.send import sendFeedback

router = APIRouter()


# Define the request body schema
class Feedback(BaseModel):
    reason: str
    type: str


@router.post("/feedback")
async def feedback(feedback: Feedback):
    try:
        type = feedback.type
        reason = feedback.reason

        sendFeedback(type, reason)

        return {"success": True}
    except Exception:
        return {"success": False}
