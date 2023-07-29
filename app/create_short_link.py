import uuid


def generate_short_link(length=8):
    # UUID  Generation
    short_link = str(uuid.uuid4()).replace('-', '')[:length]
    return short_link
