import typesense

client = typesense.Client(
    {
        "nodes": [
            {
                "host": "localhost",  # For Typesense Cloud use xxx.a1.typesense.net
                "port": "8108",  # For Typesense Cloud use 443
                "protocol": "http",  # For Typesense Cloud use https
            }
        ],
        "api_key": "xyz",
        "connection_timeout_seconds": 2,
    }
)

schema = {
    "name": "entreprise",
    "fields": [
        {"name": "id", "type": "int32"},
        {"name": "rid", "type": "string"},
        {"name": "designation", "type": "string"},
        {"name": "sigle", "type": "string"},
        {"name": "forme_juridique", "type": "string"},
        {"name": "code_postal_postale", "type": "string"},
        {"name": "ville_physique", "type": "string"},
        {"name": "ape", "type": "string"},
        {"name": "situation_entreprise", "type": "string"},
        {"name": "etat_rid", "type": "string"},
        {"name": "date_creation", "type": "string"},
        {"name": "date_radiation", "type": "string"},
        {"name": "motif_radiation", "type": "string"},
        {"name": "telephone", "type": "string"},
        {"name": "email", "type": "string"},
        {"name": "activites_secondaires", "type": "string"},
        {"name": "adresse_physique", "type": "string"},
        {"name": "adresse_postale", "type": "string"},
        {"name": "code_ape", "type": "string"},
    ],
}


def create_schema_collection():
    # collections = client.collections.retrieve()
    # print('collections :', collections)
    # client.collections.create(schema)

    search_parameters = {
        "q": "digit",
        "query_by": "sigle, designation",
    }

    result = client.collections["entreprise"].documents.search(search_parameters)

    print("---- RESULT ----", result)
