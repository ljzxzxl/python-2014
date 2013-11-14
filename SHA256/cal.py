import sys, hashlib, base64
from path import path

def calc_sha(obj):
    """Calculates the base64-encoded SHA hash of a file."""
    try:
        pathfile = path(obj)
    except UnicodeDecodeError:
        pathfile = None
    sha = hashlib.sha256()

    if pathfile and pathfile.exists():
        return base64.b64encode(pathfile.read_hash('SHA256'))
    elif isinstance(obj, basestring):
        sha.update(obj)
    elif hasattr(obj, 'read'):
        while True:
            d = obj.read(8192)
            if not d:
                break
            sha.update(d)
    else:
        return None

    r = sha.digest()
    r = base64.b64encode(r)
    return r

file_path = sys.argv[1]
print calc_sha(file_path)


