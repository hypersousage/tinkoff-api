from typing import Dict, Any

from tinkoff.investments.model.base import Error
from tinkoff.investments.model.response import TinkoffInvestmentsAPIResponse
from tinkoff.investments.client.exceptions import TinkoffInvestmentsAPIError


class BaseTinkoffInvestmentsAPI:
    def __init__(self, client):
        self._client = client

    async def _request(self, method, path, **kwargs):
        # type: (str, str, Any) -> Dict[Any, Any]
        # noinspection PyProtectedMember
        data = await self._client._request(method, path, **kwargs)
        response = TinkoffInvestmentsAPIResponse.from_dict(data)
        if response.is_successful():
            return response.payload
        else:
            raise TinkoffInvestmentsAPIError(
                tracking_id=response.trackingId,
                status=response.status,
                error=Error(
                    message=response.payload.get('message'),
                    code=response.payload.get('code'),
                )
            )


__all__ = [
    'BaseTinkoffInvestmentsAPI',
]