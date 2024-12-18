from app.typesense.collections import create_schema_collection_and_documents
from app.typesense.documents import create_typesense_nested_documents


def create_collections_and_documents():
    create_schema_collection_and_documents()
    create_typesense_nested_documents()
