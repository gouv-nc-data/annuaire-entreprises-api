from app.services.search.search_builder import build_search
from app.services.formatters.entreprise_results import format_result


class SearchResult:
    def __init__(self, search_params=None):
        self.search_client = None
        self.search_params = search_params
        self.results = None
        self.total_results = None
        self.run()

    def execute_search(self):
        print("executing search")

        search_results = format_result(self.search_client)

        print("search result in search result service : ", search_results)

        self.total_results = len(search_results)
        self.results = search_results

    def run(self):
        build_search(self)
        self.execute_search()
