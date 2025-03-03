# GoTotus.com APIs' Python bindings

_Status:_ beta, to be released.

## Basic Usage

`TOTUS_KEY` environment variable will be used to pick the api
key ([create one here](https://gototus.com/console/apikeys))

```python
from totus import Totus
import pprint

t = Totus()  # picks the key from TOTUS_KEY envar
t = Totus(api_key="<your-api-key>")

reference = t.Reference()  # the Refence sets of APIs

results = reference.GeoPOI(gh='69y7pkxfc', distance=1000, what='shop', limit=10)

pprint.pp(results)
```

For detailed manuals please check: [docs.gototus.com](https://docs.gototus.com)

## Installing

At the moment you will need to checkout this repository and do:
`pip install -e <path-to-checkout>`.

Soon: `pip install totus`

## Building

```
make setup build 
[...]
make clean
```

for building, you will need to have a functioning Totus API key.