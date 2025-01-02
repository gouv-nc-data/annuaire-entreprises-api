from fastapi import APIRouter, Request
from loguru import logger

from app.typesense.create_collections_and_documents import (
    create_collections_and_documents,
)

router = APIRouter()


@router.post("/typesense/init", status_code=201)
async def typesense_init(request: Request):
    logger.debug("debut indexation")
    create_collections_and_documents()
    logger.info("fin indexation")
    return {"status": "ok"}
