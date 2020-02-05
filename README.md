# tinkoff-api

> Python Tinkoff API client for asyncio and humans.

[![Latest Version](https://img.shields.io/pypi/v/tinkoff-api.svg)](https://pypi.python.org/pypi/tinkoff-api)
[![Python Version](https://img.shields.io/pypi/pyversions/tinkoff-api.svg)](https://pypi.python.org/pypi/tinkoff-api)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


In active development.

Table of contens
--------------------------------------------------------------------------------
* [Installation](#installation)
* [Usage example](#usage-example)

Installation
--------------------------------------------------------------------------------

Use pip to install:
```shell
$ pip install tinkoff-api
```

Usage example
--------------------------------------------------------------------------------

```python
import asyncio
from datetime import datetime

from tinkoff.investments.client import TinkoffInvestmentsRESTClient
from tinkoff.investments.model.market.candles import Candles, CandleResolution
from tinkoff.investments.client.exceptions import TinkoffInvestmentsError

client = TinkoffInvestmentsRESTClient(token='TOKEN')

async def apple_year_candles() -> Candles:
    try:
        candles = await client.market.candles.get(
            figi='BBG000B9XRY4',
            dt_from=datetime(2019, 1, 1),
            dt_to=datetime(2019, 12, 31),
            interval=CandleResolution.DAY
        )
        return candles
    except TinkoffInvestmentsError as e:
        print(e)

asyncio.run(apple_year_candles())
```

TODO
--------------------------------------------------------------------------------

* cover full Tinkoff Investments API
* add context manager for rest client
* add streaming protocol client
* generate documentation