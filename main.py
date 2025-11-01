from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services import CatalogService
from src.logger import logger


catalog_service = CatalogService()

origins=["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def main():
    return {"Hello": "World"}


@app.get("/catalog")
async def get_gatalog():
    return catalog_service.get_catalog()

