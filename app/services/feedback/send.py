from app.database import models
from app.database.connection import SessionLocal

db = SessionLocal()


def sendFeedback(type: str, reason: str):
    Feedback = models.Feedback

    new_feedback = Feedback(type=type, reason=reason)

    db.add(new_feedback)
    db.commit()
