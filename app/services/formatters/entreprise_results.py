def format_result(items):
    results = []

    for item in items:
        results.append({"entreprise": item.__dict__})

    return results


def format_result_typesense(items):
    results = []

    for item in items:
        results.append({"entreprise": item['document']})

    return results
