# Gearbest Api

A simple wrapper for gearbest api in python

## Installing
```
$ pipenv install gearbest-api
```

## A Simple Example
```
from gearbest_api import GearbestApi

gearbest_api = GearbestApi(api_key='1234', api_secret='secret')
gearbest_api.get_app_exclusive_price_product()

```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
