# GoTotus.com APIs' Python bindings

## Basic Usage

`TOTUS_KEY` environment variable will be used to pick the api
key ([create one here](https://gototus.com/console/apikeys))

```python
from totus import Totus

t = Totus()  # picks the key from TOTUS_KEY envar
t = Totus(api_key="<your-api-key>")

reference = t.Reference()  # the Reference set of APIs

print(reference.GeoPOI(gh='69y7pkxfc', distance=1000, what='shop', limit=2))
```

it will print:

```json
[
  {
    "id": 4675113766,
    "lat": -34.60362,
    "lon": -58.3824,
    "gh": "69y7pkx5r3",
    "dist": 71.6,
    "info": {
      "addr:city": "Ciudad Aut\u00f3noma de Buenos Aires",
      "addr:country": "AR",
      "addr:street": "Avenida Corrientes",
      "name": "Maxikiosko",
      "shop": "kiosk"
    }
  },
  {
    "id": 12179098601,
    "lat": -34.60395,
    "lon": -58.38076,
    "gh": "69y7ps83ms",
    "dist": 84,
    "info": {
      "addr:housenumber": "999",
      "addr:street": "Avenida Presidente Roque S\u00e1enz Pe\u00f1a",
      "name": "I Love Gifts",
      "shop": "gift"
    }
  }
]
```

## Examples

For further examples, check the `examples/` folder in this project.
Or a public copy at the [GitHub Website](https://github.com/GoTotus/pytotus/tree/main/examples).

## Manuals

For detailed manuals about Totus please check: [docs.gototus.com](https://docs.gototus.com)

## Installing

`pip install totus`

## Building

```
make setup build 
[...]
make clean
```

Local Test: `pip install -e <src_folder>`.

for building, you will need to have a functioning Totus API key in the envvar `TOTUS_KEY`.
