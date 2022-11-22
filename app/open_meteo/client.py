from typing import Dict, Any

from aiohttp import ClientSession, ClientTimeout

from app.config import settings
from app.open_meteo.models import Forecast

Params = Dict[str, Any] | None


class OpenMeteoClient:
    def __init__(self, timeout: int = 30) -> None:
        self._base_url = settings.open_meteo_api_url
        self._session: ClientSession = ClientSession(timeout=ClientTimeout(total=timeout))

    async def _request(
        self,
        method: str,
        params: Dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        if params is None:
            params = {}
        assert self._session, f"{self} not connected"

        url = self._base_url
        async with self._session.request(method, url, params=params, **kwargs) as resp:
            text_payload = await resp.text()
            print(f"Received: {method.upper()} {url} {resp.status} " f"body={text_payload}")
            if resp.ok:
                return await resp.json() if text_payload else None
            else:
                raise Exception(resp.status, text_payload)

    async def _get(self, params: Params = None, **kwargs: Any) -> Any:
        return await self._request("GET", params=params, **kwargs)

    async def get_forecast_all_values(self, params: Dict[str, Any]) -> Forecast:
        result: Dict[str, Any] = await self._get(params=params)
        return Forecast.parse_obj(result)


client = OpenMeteoClient()
