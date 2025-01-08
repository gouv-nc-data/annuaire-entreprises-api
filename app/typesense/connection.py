import typesense
from app.config import settings

typesense_settings = settings.typesense


typesense_client = typesense.Client(
    {
        "nodes": [
            {
                "host": typesense_settings.typesense_api_host,  # For Typesense Cloud use xxx.a1.typesense.net
                "port": typesense_settings.typesense_api_port,  # For Typesense Cloud use 443
                "protocol": "http",  # For Typesense Cloud use https
            }
        ],
        "api_key": typesense_settings.typesense_api_key,
        "connection_timeout_seconds": 36000,
        "healthy-read-lag":100000,
        "healthy-write-lag":100000,
    }
)
