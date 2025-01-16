def format_dirigeant_nom_complet(
    prenoms=None,
    nom=None,
):

    if not prenoms:
        nom_complet = ""
    else:
        nom_complet = prenoms

    # Add sigle if it exists
    if nom:
        nom_complet += f" {nom}"

    return nom_complet.upper()
