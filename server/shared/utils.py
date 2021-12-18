import hashlib


def title_to_id(title):
    return int(hashlib.sha1(title.encode("utf-8")).hexdigest(), 16) % (10 ** 8)