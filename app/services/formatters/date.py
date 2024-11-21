import locale

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


def format_date(date=None):

    if not date:
        return None

    string_date = str(date)

    return string_date
