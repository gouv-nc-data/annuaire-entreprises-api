from app.services.search.queries.search_by_ridet import search_by_ridet
from app.services.search.search_builder import build_search


class SearchResult:
    def __init__(self, search_params=None):
        self.search_kind = None
        self.search_params = search_params
        self.results = None
        self.total_results = None
        self.run()

    def execute_search(self):
        print("executing search")
        print("search kind : ", self.search_kind)

        search_results = search_by_ridet(self.search_params)

        self.total_results = len(search_results)
        self.results = search_results

    def run(self):
        build_search(self)
        self.execute_search()
