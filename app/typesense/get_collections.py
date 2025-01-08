from app.typesense.connection import typesense_client
from loguru import logger


def get_collections():
    try:

        print('typesense_client', typesense_client)

        collections = typesense_client.collections.retrieve()
    except Exception as e:
        logger.exception(
            "An error occurred during retrieving collections for typesense:"
        )

        print('error in collections : ', e)

        raise e

    print("Typesense collections : ", collections)

    return collections
