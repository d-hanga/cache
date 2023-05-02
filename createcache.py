import json

def dict(data, cache_filename):
    with open(cache_filename, 'w') as f:
        json.dump(data, f)
    return data
