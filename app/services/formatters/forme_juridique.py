from app.labels.helpers import FORME_JURIDIQUES


def format_forme_juridique(forme_juridique):
    if forme_juridique not in FORME_JURIDIQUES:
        return None
    else:
        return forme_juridique
