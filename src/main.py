from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.breads import bread_routes

app = FastAPI()

origins = [
    "http://192.168.0.10:3000",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(bread_routes)
