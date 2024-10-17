def format_nom_complet(
    enseigne=None,
    sigle=None,
):
    if not enseigne:
        return None

    nom_complet = enseigne

    # Add sigle if it exists
    if sigle:
        nom_complet += f" ({sigle})"

    return nom_complet.upper()
