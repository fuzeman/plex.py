# plex.py

[![](https://travis-ci.org/fuzeman/plex.py.svg?branch=master)](https://travis-ci.org/fuzeman/plex.py) [![Coverage Status](https://coveralls.io/repos/fuzeman/plex.py/badge.png?branch=master)](https://coveralls.io/r/fuzeman/plex.py?branch=master)

Python interface for the Plex Media Server API.


## Usage

Quick example *(connects to your local server)*:

```python
from plex import Plex

for item in Plex['library'].recently_added():
    print '[%s] %s' % (item.type, item.title)
```

Connect to a remote server:
```python
from plex import Plex

with Plex.configuration.server(host='192.168.1.110'):
    recently_added = Plex['library'].recently_added()

    for item in recently_added:
        print '[%s] %s' % (item.type, item.title)
```

## Testing

Install requirements:
```
pip install -r requirements.txt
pip install -r requirements_test.txt
```

Unit tests:
```
py.test
```

Unit tests (via *coverage.py*):
```
coverage run -m py.test
```

## License

```
The MIT License (MIT)

Copyright (c) 2014 Dean Gardiner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```