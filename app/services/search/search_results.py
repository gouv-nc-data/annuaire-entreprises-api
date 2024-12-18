from app.database.connection import SessionLocal

from app.services.search.search_builder import build_search
from app.services.formatters.entreprise_results import (
    format_result,
    format_result_typesense,
)

from app.services.search.queries.execute_query import execute_sqlalchemy_query
from app.services.search.typesense.execute_query import execute_typesense_query

import typesense

db = SessionLocal()

typesense_client = typesense.Client(
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


class SearchResult:
    def __init__(self, search_params=None):
        self.search_client = None
        self.search_params = search_params
        self.results = None
        self.total_results = None
        self.run()

    def execute_search(self):
        # sql_alchemy_query = execute_sqlalchemy_query(
        #     db, self.search_client, self.search_params
        # )

        typesense_query = execute_typesense_query(
            typesense_client, self.search_client, self.search_params
        )

        # search_results = format_result(sql_alchemy_query["results"])

        search_results = format_result_typesense(typesense_query["results"])

        # print("RESULTS typesense", search_results_typesense)

        self.total_results = typesense_query["total_results"]
        self.results = search_results

    def run(self):
        build_search(self)
        self.execute_search()
