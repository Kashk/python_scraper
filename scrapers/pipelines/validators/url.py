import validators

def is_valid_url(url):
    if url is not None:
        return validators.url(url)
    return False

def is_not_valid_url(url):
    return not is_valid_url(url)
