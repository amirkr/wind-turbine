import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.anyio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 307
    assert response.headers["Location"] == "/docs"
