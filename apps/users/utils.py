
def get_slug_text(first_name, last_name):
    slug_text = None
    if first_name and last_name:
        slug_text = "{}{}".format(first_name.lower(), last_name.lower())

    assert slug_text is not None,\
        "There must be a field named `first_name` and `last_name`"
    return slug_text
