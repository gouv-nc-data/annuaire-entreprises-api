from fastapi import APIRouter, Request
from loguru import logger

from app.typesense.create_collections_and_documents import (
    create_collections_and_documents,
)

from app.typesense.get_collections import get_collections

router = APIRouter()


@router.post("/typesense/init", status_code=201)
async def typesense_init(request: Request):
    logger.debug("debut indexation")
    create_collections_and_documents()
    logger.info("fin indexation")
    return {"status": "ok"}


@router.get("/typesense/collections", status_code=200)
async def typesense_retrieve_collections(request: Request):
    logger.debug("debut collectionss")
    collections = get_collections()
    logger.info("fin collections")
    return collections
