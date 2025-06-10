from app.database import models
from app.database.connection import LocalSession
from fastapi import Depends
from sqlalchemy.orm import Session
from loguru import logger

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        LocalSession.remove()

def signup(email: str, reason: str, db: Session = Depends(get_db)):
    AgentPublic = models.AgentPublic

    new_agent_public = AgentPublic(email=email, reason=reason)

    db.add(new_agent_public)
    db.commit()
