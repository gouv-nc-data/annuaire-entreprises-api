from app.models.response import ResponseModel
from app.services.format_search_results import format_search_results


class ResponseBuilder:
    def __init__(self, search_params, results):
        self.total_results = min(int(results.total_results), 10000)
        self.per_page = search_params.per_page
        self.results = format_search_results(results, search_params)
        self.page = search_params.page
        self.total_pages = self.calculate_total_pages()
        response = ResponseModel(
            results=self.results,
            total_results=self.total_results,
            page=self.page,
            per_page=self.per_page,
            total_pages=self.total_pages,
        )
        self.response = response.model_dump(exclude_unset=True)

    def calculate_total_pages(self):
        quotient, remainder = divmod(
            self.total_results,
            self.per_page,
        )
        total_pages = quotient + 1 if remainder > 0 else quotient
        return total_pages
