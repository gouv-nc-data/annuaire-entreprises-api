import re

from pydantic import BaseModel, field_validator, model_validator

from app.controllers.field_validation import (
    FIELD_LENGTHS,
    NUMERIC_FIELD_LIMITS,
    VALID_FIELD_VALUES,
)
from app.exceptions.exceptions import InvalidParamError
from app.utils.helpers import (
    check_params_are_none_except_excluded,
    clean_str,
    str_to_list,
)


class SearchParams(BaseModel):
    """Class for modeling search parameters"""

    terms: str | None = None
    page: int = 1
    per_page: int = 10
    ville: list | None = None
    code_postal: list | None = None
    forme_juridique: list | None = None
    code_ape: list | None = None
    etat_rid: str | None = None
    dirigeant: str | None = None
    type_structure: str | None = None

    # Field Validators (involve one field at a time)
    @field_validator("page", "per_page", mode="before")
    def cast_as_integer(cls, value: str, info) -> int:
        try:
            int(value)
        except ValueError:
            raise InvalidParamError(
                f"Veuillez indiquer un paramètre `{info.field_name}` entier."
            )
        return int(value)

    @field_validator(
        "page",
        "per_page",
        mode="after",
    )
    # Apply after first validator and Pydantic internal validation
    def check_if_number_in_range(cls, value, info):
        limits = NUMERIC_FIELD_LIMITS.get(info.field_name)
        if value < limits.get("min") or value > limits.get("max"):
            raise InvalidParamError(
                f"Veuillez indiquer un paramètre `{info.field_name}` entre "
                f"`{limits.get('min')}` et `{limits.get('max')}`, "
                f"par défaut `{limits['default']}`."
            )
        return value

    @field_validator(
        "terms",
        mode="before",
    )
    def make_uppercase(cls, value: str) -> str:
        return value.upper()

    @field_validator("dirigeant", mode="before")
    def clean_name(cls, value: str) -> str:
        return value.replace("-", " ").lower()

    @field_validator(
        "ville",
        "code_postal",
        "code_ape",
        mode="before",
    )
    def convert_str_to_upper_list(cls, str_of_values: str) -> list[str]:
        list_of_values = str_to_list(clean_str(str_of_values))
        return list_of_values

    @field_validator(
        "forme_juridique",
        mode="before",
    )
    def convert_str_to_list(cls, str_of_values: str) -> list[str]:
        list_of_values = str_to_list(str_of_values.upper())
        return list_of_values

    @field_validator(
        "etat_rid",
        mode="before",
    )
    def convert_str_to_upper(cls, str: str) -> str:
        return str.upper()

    @field_validator(
        "type_structure",
        mode="before",
    )
    def convert_str_to_upper_and_replace_spaces(cls, str: str) -> str:
        str = str.replace(" ", "_")
        return str.upper()

    @field_validator(
        "etat_rid",
        "type_structure",
        mode="after",
    )
    def value_must_be_valid(cls, value: str, info) -> str:
        valid_values = VALID_FIELD_VALUES.get(info.field_name)["valid_values"]
        if value not in valid_values:
            raise InvalidParamError(
                f"Le paramètre "
                f"`{VALID_FIELD_VALUES.get(info.field_name)['alias']}` "
                f"est non valide. "
                f"Les valeurs valides : {[value for value in valid_values]}."
            )

        return value

    @field_validator("code_postal", "ville", mode="after")
    def list_of_values_should_match_regular_expression(
        cls, list_values: list[str], info
    ) -> list[str]:
        for value in list_values:
            valid_values = VALID_FIELD_VALUES.get(info.field_name)["valid_values"]
            if not re.search(valid_values, value):
                raise InvalidParamError(
                    f"Au moins une valeur du paramètre {info.field_name} "
                    "est non valide."
                )
        return list_values

    @field_validator(
        "forme_juridique",
        "code_ape",
        mode="after",
    )
    def list_of_values_must_be_valid(cls, list_of_values: list[str], info) -> list[str]:
        valid_values = VALID_FIELD_VALUES.get(info.field_name)["valid_values"]
        for value in list_of_values:
            if value not in valid_values:
                raise InvalidParamError(
                    f"Au moins un paramètre "
                    f"`{VALID_FIELD_VALUES.get(info.field_name)['alias']}` "
                    f"est non valide. "
                    f"Les valeurs valides : {[value for value in valid_values]}."
                )
        return list_of_values

    @field_validator(
        "code_ape",
        mode="after",
    )
    def transform_code_ape(cls, list_of_values: list[str], info) -> list[str]:
        transformed_values = []

        for value in list_of_values:
            if value is not None:
                transformed_values.append(value.replace(".", ""))

        return transformed_values

    # Model Validators (involve more than one field at a time)
    @model_validator(mode="after")
    def total_results_should_be_smaller_than_10000(self):
        page = self.page
        per_page = self.per_page
        if page * per_page > NUMERIC_FIELD_LIMITS["total_results"]["max"]:
            raise InvalidParamError(
                "Le nombre total de résultats est restreint à 10 000. "
                "Pour garantir cela, le produit du numéro de page "
                "(par défaut, page = 1) et du nombre de résultats par page "
                "(par défaut, per_page = 10), c'est-à-dire `page * per_page`, "
                "ne doit pas excéder 10 000."
            )
        return self

    @model_validator(mode="after")
    def check_if_all_empty_params(self):
        """
        If all parameters are empty (except matching size and pagination
        because they always have a default value) raise value error
        Check if all non-default parameters are empty, raise a InvalidParamError
        if they are
        """
        excluded_fields = [
            "page",
            "per_page",
        ]

        all_fields_are_null_except_excluded = check_params_are_none_except_excluded(
            self.dict(exclude_unset=True), excluded_fields
        )
        if all_fields_are_null_except_excluded:
            raise InvalidParamError(
                "Veuillez indiquer au moins un paramètre de recherche."
            )
        return self

    @model_validator(mode="after")
    def check_if_short_terms_and_no_other_param(self):
        """Prevent performance issues by refusing query terms less than 3 characters.
        Accept less than 3 characters if at least one parameter is filled.
        Except matching size, because this param always has a default value.
        """
        # List of parameters to exclude from the check
        excluded_fields = [
            "page",
            "per_page",
            "terms",
        ]

        all_fields_are_null_except_excluded = check_params_are_none_except_excluded(
            self.dict(exclude_unset=True), excluded_fields
        )
        if (
            self.terms is not None
            and len(self.terms) < FIELD_LENGTHS["terms"]
            and all_fields_are_null_except_excluded
        ):
            raise InvalidParamError(
                "3 caractères minimum pour les termes de la requête "
                + "(ou utilisez au moins un filtre)"
            )
        return self
