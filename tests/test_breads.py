import pytest
from httpx import AsyncClient
from src.main import app

record = {
    "name": "Canxin",
}


@pytest.mark.asyncio
async def test_sum():
    a= 10
    b= 10
    c = a+b
    assert c ==20
# @pytest.mark.asyncio
# async def test_create_bread():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/bread/", json=record)
#     assert response.status_code == 201


# @pytest.mark.asyncio
# async def test_duplicate_bread():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/bread/", json=record)
#     assert response.status_code == 400


# @pytest.mark.asyncio
# async def test_list_breads():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/bread/")
#     assert response.status_code == 200


# @pytest.mark.asyncio
# async def test_list_breads_pagination():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/bread/?offset=0&limit=100")
#     assert response.status_code == 200


# @pytest.mark.asyncio
# async def test_list_breads_pagination_limit():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/bread/?offset=0&limit=1")
#         count_result = len(response.json())
#     assert count_result == 1


# @pytest.mark.asyncio
# async def test_list_breads_offset_pagination():
#     async with AsyncClient(app=app, base_url="http://test") as ax:  # cache -> check
#         response = await ax.get("/products/?offset=1&limit=1")
#         product = response.json()[0]["name"]
#     assert product == "lapis"


# @pytest.mark.asyncio
# async def test_update_by_name():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.patch(
#             "/bread/update/Canxin",
#             json={"name": "Tabapua"}
#         )

#         product = response.json()["name"]
#     assert product == "Tabapua"


# @pytest.mark.asyncio
# async def test_delete_by_name():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.delete(
#             "/bread/delete/Tabapua",
#         )
#     assert response.status_code == 204
