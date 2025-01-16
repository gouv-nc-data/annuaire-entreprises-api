from app.labels.helpers import CODES_NAF, FORME_JURIDIQUES

NUMERIC_FIELD_LIMITS = {
    "page": {"min": 1, "max": 1000, "default": 1, "alias": "page"},
    "per_page": {"min": 1, "max": 25, "default": 10, "alias": "per_page"},
    "total_results": {"min": 0, "max": 10000},
}

VALID_FIELD_VALUES = {
    "forme_juridique": {
        "valid_values": FORME_JURIDIQUES,
        "alias": "forme_juridique",
    },
    "ville": {
        "valid_values": r"^[a-zA-Z]+$",
        "alias": "ville_physique",
    },
    "code_postal": {
        "valid_values": r"^((0[1-9])|([1-8][0-9])|(9[0-8])|(2A)|(2B))[0-9]{3}$",
        "alias": "code_postal",
    },
    "activite_principale": {
        "valid_values": CODES_NAF,
        "alias": "activite_principale",
    },
    "etat_rid": {
        "valid_values": ["I", "R"],
        "alias": "etat_rid",
    },
}

FIELD_LENGTHS = {
    "code_postal": 5,
    "terms": 3,
}
