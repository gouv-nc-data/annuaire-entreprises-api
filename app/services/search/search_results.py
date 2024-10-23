from app.database.connection import SessionLocal

from app.services.search.search_builder import build_search
from app.services.formatters.entreprise_results import format_result

from app.services.search.queries.execute_query import execute_sqlalchemy_query

db = SessionLocal()


class SearchResult:
    def __init__(self, search_params=None):
        self.search_client = None
        self.search_params = search_params
        self.results = None
        self.total_results = None
        self.run()

    def execute_search(self):
        sql_alchemy_query = execute_sqlalchemy_query(
            db, self.search_client, self.search_params
        )

        search_results = format_result(sql_alchemy_query["results"])

        self.total_results = sql_alchemy_query["total_results"]
        self.results = search_results

    def run(self):
        build_search(self)
        self.execute_search()
