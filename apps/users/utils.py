from hashlib import md5


def generate_gravatar_url(email=None):
    if not email:
        raise ValueError("Email can't be blank")

    url = "https://www.gravatar.com/avatar/"
    url += md5(email.lower().encode('utf-8')).hexdigest()
    url += '?s=400&d=identicon'
    return url
