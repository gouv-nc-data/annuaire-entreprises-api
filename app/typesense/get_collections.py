from app.typesense.connection import typesense_client
from loguru import logger


def get_collections():
    try:
        collections = typesense_client.collections.retrieve()
    except Exception as e:
        logger.exception(
            "An error occurred during retrieving collections for typesense:"
        )

        raise e

    return collections
