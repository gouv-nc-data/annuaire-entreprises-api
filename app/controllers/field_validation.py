from app.labels.helpers import FORME_JURIDIQUES

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
    "commune": {
        "valid_values": r"^([013-9]\d|2[AB1-9])\d{3}$",
        "alias": "commune",
    },
    "code_postal": {
        "valid_values": r"^((0[1-9])|([1-8][0-9])|(9[0-8])|(2A)|(2B))[0-9]{3}$",
        "alias": "activite_principale",
    },
}

FIELD_LENGTHS = {
    "code_postal": 5,
    "terms": 3,
}
