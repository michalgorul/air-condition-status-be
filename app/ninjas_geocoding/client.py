from typing import Dict, Any, List

from aiohttp import ClientSession, ClientTimeout
from fastapi import HTTPException

from app.config import settings

Params = Dict[str, Any] | None


class NinjasClient:
    def __init__(self, timeout: int = 30) -> None:
        self.api_key = settings.ninjas_api_key
        self._base_url = settings.ninjas_api_url
        headers: Dict[str, str] = {"X-Api-Key": self.api_key}
        self._session: ClientSession = ClientSession(
            timeout=ClientTimeout(total=timeout), headers=headers
        )

    async def _request(
        self,
        method: str,
        data: Any = None,
        params: Dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        if params is None:
            params = {}
        assert self._session, f"{self} not connected"

        url = self._base_url
        async with self._session.request(method, url, params=params, json=data, **kwargs) as resp:
            text_payload = await resp.text()
            print(f"Received: {method.upper()} {url} {resp.status} " f"body={text_payload}")
            if resp.ok:
                return await resp.json() if text_payload else None
            else:
                raise HTTPException(status_code=resp.status, detail=text_payload)

    async def _get(self, params: Params = None, **kwargs: Any) -> Any:
        return await self._request("GET", params=params, **kwargs)

    async def get_geolocation(self, city: str, country: str | None) -> List[Dict[str, Any]]:
        city = {"city": city}
        country = {"country": country} if country else {}
        params = city | country
        result = await self._get(params=params)
        return result


client = NinjasClient()
