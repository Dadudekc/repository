"""API client utilities for the unified workspace."""
from __future__ import annotations

import asyncio
from typing import Any, Dict, Optional

import aiohttp
import requests

from .config import get_setting


class APIClient:
    """Synchronous API client."""

    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        self.base_url = base_url
        self.api_key = api_key or get_setting("API_KEY")
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        """Perform a GET request."""
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint: str, data: Dict[str, Any], **kwargs: Any) -> requests.Response:
        """Perform a POST request."""
        return self.session.post(f"{self.base_url}{endpoint}", json=data, **kwargs)


class AsyncAPIClient:
    """Asynchronous API client."""

    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        self.base_url = base_url
        self.api_key = api_key or get_setting("API_KEY")
        self.headers: Dict[str, str] = {}
        if self.api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"

    async def get(self, endpoint: str, **kwargs: Any) -> aiohttp.ClientResponse:
        url = f"{self.base_url}{endpoint}"
        async with aiohttp.ClientSession() as session:
            return await session.get(url, headers=self.headers, **kwargs)

    async def post(self, endpoint: str, data: Dict[str, Any], **kwargs: Any) -> aiohttp.ClientResponse:
        url = f"{self.base_url}{endpoint}"
        async with aiohttp.ClientSession() as session:
            return await session.post(url, json=data, headers=self.headers, **kwargs)
