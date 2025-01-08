from app.database import models
from app.database.connection import SessionLocal

db = SessionLocal()


def signup(email: str, reason: str):
    AgentPublic = models.AgentPublic

    new_agent_public = AgentPublic(email=email, reason=reason)

    db.add(new_agent_public)
    db.commit()
