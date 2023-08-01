from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.script_launch import router as script_router

from ..settings import Settings


settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=str(settings.CORS_ALLOW_CREDENTIALS),
    allow_methods=str(settings.CORS_ALLOW_METHODS),
    allow_headers=str(settings.CORS_ALLOW_HEADERS),
)

app.include_router(script_router, prefix='', tags=['User'])
