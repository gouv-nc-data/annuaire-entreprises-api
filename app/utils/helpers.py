def str_to_list(string_values: str) -> list[str]:
    values_list = string_values.split(",")
    return values_list


def clean_str(param: str):
    param = param.replace("-", " ")
    param_clean = param.replace(" ", "").upper()
    return param_clean


def check_params_are_none_except_excluded(fields_dict, excluded_fields):
    for key, value in fields_dict.items():
        if key not in excluded_fields and value is not None:
            return False
    return True


def get_value(data_dict, key, default=None):
    """
    Get the value associated with the given key from the dictionary.
    """
    if not data_dict:
        return default
    return data_dict.get(key, default)


def string_list_to_string(string_list):
    if string_list is None:
        return None
    elif string_list.strip("[]") == "nan":
        return None
    else:
        elements = string_list.strip("[]").split(", ")
        # Remove surrounding quotes from each element
        cleaned_elements = [element.strip("'") for element in elements]
        # Join the elements into a single string
        return ", ".join(cleaned_elements)
