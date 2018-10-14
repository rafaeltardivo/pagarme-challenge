import re


def is_alpha_or_space(value):
    """Validates for only alphanumerics with/without spaces."""

    expression = re.compile("^[a-zA-Z ]*$")
    return len(value) and expression.match(value)
