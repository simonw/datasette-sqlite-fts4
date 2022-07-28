from datasette.app import Datasette
import pytest
import urllib


@pytest.mark.asyncio
async def test_sqlite_fts4():
    ds = Datasette(memory=True)
    response = await ds.client.get(
        "/_memory.json?"
        + urllib.parse.urlencode(
            {
                "sql": "select decode_matchinfo(x'02000000') as decoded",
                "_shape": "array",
            }
        )
    )
    assert response.status_code == 200
    assert response.json() == [{"decoded": "[2]"}]
