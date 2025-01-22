from app.database.connection import SessionLocal

from app.services.search.search_builder import build_search
from app.services.formatters.entreprise_results import (
    format_result_sql_alchemy,
    format_result_typesense,
)

from app.services.search.typesense.execute_query import execute_typesense_query
from app.services.search.queries.execute_filter_query import execute_sqlalchemy_query

from app.typesense.connection import typesense_client


db = SessionLocal()


class SearchResult:
    def __init__(self, search_params=None):
        self.search_client = None
        self.search_query = None
        self.search_params = search_params
        self.results = None
        self.total_results = None
        self.run()

    def execute_search(self):

        if self.search_client == "typesense":
            query = execute_typesense_query(
                typesense_client, self.search_query, self.search_params
            )
            search_results = format_result_typesense(query["results"])
        elif self.search_client == "sqlalchemy":
            query = execute_sqlalchemy_query(db, self.search_query, self.search_params)
            search_results = format_result_sql_alchemy(query["results"])

        self.total_results = query["total_results"]
        self.results = search_results

    def run(self):
        build_search(self)
        self.execute_search()
