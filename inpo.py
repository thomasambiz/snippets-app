import logging
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
# Set the log output file, and the log level

def put(name, snippet):
    """
    Store a snippet with an associated name.
    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet