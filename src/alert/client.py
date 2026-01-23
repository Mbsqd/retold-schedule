import time

import httpx

from src.alert.enums import AlertStatusResponseEnum


class AlertClient:
    def __init__(self, token: str, base_url: str, cache_ttl: int = 10) -> None:
        self.token = token
        self.base_url = base_url
        self.cache_ttl = cache_ttl
        self._cache: dict[int, tuple[float, AlertStatusResponseEnum]] = {}
        self._client: httpx.AsyncClient | None = None

    async def start(self):
        if self._client is None:
            self._client = httpx.AsyncClient(timeout=5)

    async def stop(self) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None

    async def get_air_raid_status(self, uid: int) -> AlertStatusResponseEnum:
        now = time.time()

        if uid in self._cache:
            cached_at, cached_value = self._cache[uid]
            if now - cached_at < self.cache_ttl:
                return cached_value

        if not self._client:
            raise RuntimeError("Client not initialized")

        url = f"{self.base_url}/active_air_raid_alerts/{uid}.json"
        params = {"token": self.token}

        response = await self._client.get(url, params=params)
        response.raise_for_status()

        value = response.json()
        data = AlertStatusResponseEnum(value)

        self._cache[uid] = (now, data)

        return data
