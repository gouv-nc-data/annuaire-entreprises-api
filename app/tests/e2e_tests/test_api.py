import pytest

from app.tests.e2e_tests.resonse_tester import APIResponseTester

# All tests are based on fake data
# TODO adjust tests with valid values with production database

fake_entreprise = {
    "nom_complet": "GUILLOT SA (MOULIN ET ROBERT)",
    "rid": "984766",
    "sigle": "Moulin et Robert",
    "enseigne": "Guillot SA",
    "forme_juridique": "voluptates",
    "adresse_complete": "66 Allée Marcadet, Drancy, 98071",
    "adresse": "66 Allée Marcadet",
    "code_postal": "98071",
    "ville": "Drancy",
}


@pytest.fixture
def api_response_tester():
    api_url = "http://localhost:8000/api/v1/"
    return APIResponseTester(api_url)


def test_fetch_entreprise_by_sigle(api_response_tester):
    """
    test if searching for `Moulin et Robert` returns the right ridet as the first search result.
    """
    path = "recherche?q=" + fake_entreprise["sigle"]
    api_response_tester.test_field_value(path, 0, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_ridet(api_response_tester):
    """
    test if searching for ridet `984766` returns the right the fullname as the first search result.
    """
    path = "recherche?q=" + fake_entreprise["ridet"]
    api_response_tester.test_field_value(
        path, 0, "nom_complet", fake_entreprise["nom_complet"]
    )
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_enseigne(api_response_tester):
    """
    test if searching for `Robert SCOP` returns the right ridet as the first search result.
    """
    path = "recherche?q=" + fake_entreprise["enseigne"]
    api_response_tester.test_field_value(path, 1, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_entreprise_by_ville(api_response_tester):
    """
    test if searching for `Robert SCOP` returns the right ridet as the first search result.
    """
    path = "recherche?ville=Avignon"
    api_response_tester.test_number_of_results(path, 10)


def test_fetch_entreprise_by_code_postal(api_response_tester):
    """
    test if searching for `Robert SCOP` returns the right ridet as the first search result.
    """
    path = "recherche?code_postal=" + fake_entreprise["code_postal"]
    api_response_tester.test_field_value(path, 0, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_entreprise_by_forme_juridique(api_response_tester):
    """
    test if searching for `Guillot SA` returns the right ridet as the first search result.
    """
    path = "recherche?forme_juridique=" + fake_entreprise["code_postal"]
    api_response_tester.test_field_value(path, 0, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 6)


def test_fetch_by_terms(api_response_tester):
    """
    test if searching for terms `robert` returns the at least 10 results.
    """
    path = "recherche?q=robert"
    api_response_tester.assert_api_response_code_200(path)
    api_response_tester.test_number_of_results(path, 10)


def test_fetch_by_terms_case_insensitive(api_response_tester):
    """
    test if searching for terms `ROBERT` also returns the at least 10 results.
    """
    path = "recherche?q=ROBERT"
    api_response_tester.assert_api_response_code_200(path)
    api_response_tester.test_number_of_results(path, 10)


def test_fetch_by_terms_and_filter_by_ville(api_response_tester):
    """
    test if searching by specific term and filter by ville value returns the right Ridet as the first search result
    """
    path = "recherche?q=Moulin&ville=" + fake_entreprise["ville"]
    api_response_tester.test_field_value(path, 0, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_by_terms_and_filter_by_code_postal(api_response_tester):
    """
    test if searching by specific term and filter by code_postal value returns the right Ridet as the first search result
    """
    path = "recherche?q=Moulin&ville=" + fake_entreprise["code_postal"]
    api_response_tester.test_field_value(path, 0, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_by_terms_and_filter_by_forme_juridique(api_response_tester):
    """
    test if searching by specific term and filter by forme_juridique value returns the right Ridet as the first search result
    """
    path = "recherche?q=Moulin&forme_juridique=" + fake_entreprise["forme_juridique"]
    api_response_tester.test_field_value(path, 0, "ridet", fake_entreprise["ridet"])
    api_response_tester.test_number_of_results(path, 1)


def test_accept_three_characters(api_response_tester):
    """
    test if API returns results for a three character query.
    """
    path = "recherche?q=abc"
    api_response_tester.assert_api_response_code_200(path)


def test_query_too_short(api_response_tester):
    """
    test if API returns an error for a two character query
    """
    path = "recherche?q=ab"
    api_response_tester.assert_api_response_code_400(path)
    response = api_response_tester.get_api_response(path)
    assert (
        response.json()["erreur"]
        == "3 caractères minimum pour les termes de la requête "
        "(ou utilisez au moins un filtre)"
    )


def test_short_query_with_filter(api_response_tester):
    """
    test if using a filter with a two character query returns results with a filter.
    """
    path = "recherche?q=ro&forme_juridique=voluptates"
    api_response_tester.assert_api_response_code_200(path)


def test_terms_empty_only(api_response_tester):
    """
    test if searching using empty search parameters returns an error.
    """
    path = "recherche?q="
    api_response_tester.assert_api_response_code_400(path)
    response = api_response_tester.get_api_response(path)
    assert (
        response.json()["erreur"]
        == "3 caractères minimum pour les termes de la requête "
        "(ou utilisez au moins un filtre)"
    )


def test_fetch_by_terms_and_filter_by_forme_juridique_and_ville(api_response_tester):
    """
    test if searching by specific term and filter by forme_juridique and ville returns the right Ridet as the first search result
    """
    path = "recherche?q=r&forme_juridique=voluptates&ville=dunkerque"
    api_response_tester.test_field_value(path, 0, "ridet", "204663")
    api_response_tester.test_number_of_results(path, 1)


def test_fetch_by_terms_and_filter_by_forme_juridique_and_ville_and_code_postal(
    api_response_tester,
):
    """
    test if searching by specific term and filter by forme_juridique, ville and code_postal returns the right Ridet as the first search result
    """
    path = "recherche?q=r&forme_juridique=voluptates&ville=dunkerque&code_postal=98782"
    api_response_tester.test_field_value(path, 0, "ridet", "204663")
    api_response_tester.test_number_of_results(path, 1)
