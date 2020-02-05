from typing import NoReturn, Any, Dict

from aiohttp import ClientResponseError

from tinkoff.base import BaseHTTPClient
from tinkoff.investments.api import MarketAPI
from tinkoff.investments.client.environments import Environment, EnvironmentURL
from tinkoff.investments.client.exceptions import (
    TinkoffInvestmentsUnauthorizedError,
)


class TinkoffInvestmentsRESTClient(BaseHTTPClient):
    def __init__(self, token, environment=Environment.PRODUCTION):
        # type: (str, Environment) -> NoReturn
        super(TinkoffInvestmentsRESTClient, self).__init__(
            base_url=EnvironmentURL[environment],
            headers={
                'authorization': f'Bearer {token}'
            }
        )
        self.market = MarketAPI(self)

    async def _request(self, method, path, **kwargs):
        # type: (str, str, Any) -> Dict[Any, Any]
        response = await self._session.request(
            method=method,
            url=self._base_url / path.lstrip('/'),
            **kwargs
        )
        if response.status == 401:
            raise TinkoffInvestmentsUnauthorizedError
        else:
            # TODO: ловить другие исключения, если в ответе не json
            return await response.json()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()