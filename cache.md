# Introdcution

## Usage
Caching is for saving data to the disk in form of a file instead of keeping it in memory. This is useful whenever you want to save the data for later use. <br>
You can cache the data from a web API for example, to avoid making the same request again and again and possibly get banned. Or maybe it was a big and long process, that you don't want to repeat every time executing.





## Implementation
All of the caching function take a certain data-type and store it into a file.






# Technical Details

## the Code

### Cach-Creating Functions

#### Dictionary (dict)


The JSON-Library is needed to store the data in a file as JSON. <br>
```python
import json
```

Opens the file in write-mode and dumps the data into it (as JSON, so that no mistakes are happening when reading it). <br> The return value is the data that's been stored itself.
```python
def dict(data, cache_filename):
    with open(cache_filename, 'w') as f:
        json.dump(data, f)
    return data
```




### Cach-Reading Functions

#### Dictionary (dict)
```python
import json
```

Opens the file in read-mode and loads the data from it (as a dict).
```python
def dict(cache_filename):
    with open(cache_filename, 'r') as f:
        data = json.load(f)
    return data
```



