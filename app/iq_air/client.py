from typing import Dict, Any

from aiohttp import ClientSession, ClientTimeout

from app.config import settings
from fastapi import HTTPException

Params = Dict[str, Any] | None


class IQAirClient:
    def __init__(self, timeout: int = 30) -> None:
        self.api_key = settings.iq_air_api_key
        self._base_url = settings.iq_air_api_url
        self._session: ClientSession = ClientSession(timeout=ClientTimeout(total=timeout))

    async def _request(
        self,
        method: str,
        path: str,
        data: Any = None,
        params: Dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        if params is None:
            params = {}
        assert self._session, f"{self} not connected"

        url = self._base_url + path
        async with self._session.request(method, url, params=params, json=data, **kwargs) as resp:
            text_payload = await resp.text()
            print(f"Received: {method.upper()} {url} {resp.status} " f"body={text_payload}")
            if resp.ok:
                return await resp.json() if text_payload else None
            else:
                raise HTTPException(status_code=resp.status, detail=text_payload)

    async def _get(self, path: str, params: Params = None, **kwargs: Any) -> Any:
        return await self._request("GET", path, params=params, **kwargs)

    async def _post(self, path: str, data: Any, params: Params = None, **kwargs: Any) -> Any:
        return await self._request("POST", path, data=data, params=params, **kwargs)

    async def _put(self, path: str, data: Any, params: Params = None, **kwargs: Any) -> Any:
        return await self._request("PUT", path, data=data, params=params, **kwargs)

    async def _delete(self, path: str, params: Params = None, **kwargs: Any) -> Any:
        return await self._request("DELETE", path, params=params, **kwargs)

    async def get_available_states(self, country: str) -> Dict[str, Any]:
        url = "states"
        params = {"country": country, "key": self.api_key}
        result: Dict[str, Any] = await self._get(path=url, params=params)
        return result

    async def get_available_cities(self, country: str, state: str) -> Dict[str, Any]:
        url = "cities"
        params = {"state": state, "country": country, "key": self.api_key}
        result: Dict[str, Any] = await self._get(path=url, params=params)
        return result

    async def get_nearest_city_data(self) -> Dict[str, Any]:
        url = "nearest_city"
        params = {"key": self.api_key}
        result: Dict[str, Any] = await self._get(path=url, params=params)
        return result

    async def get_nearest_city_coords_data(self, lat: str, lon: str) -> Dict[str, Any]:
        url = "nearest_city"
        params = {"lat": lat, "lon": lon, "key": self.api_key}
        result: Dict[str, Any] = await self._get(path=url, params=params)
        return result

    async def get_city_data(self, country: str, state: str, city: str) -> Dict[str, Any]:
        url = "city"
        params = {"state": state, "country": country, "city": city, "key": self.api_key}
        result: Dict[str, Any] = await self._get(path=url, params=params)
        return result


client = IQAirClient()
