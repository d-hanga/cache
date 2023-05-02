import json

def dict(cache_filename):
    with open(cache_filename, 'r') as f:
        data = json.load(f)
    return data
