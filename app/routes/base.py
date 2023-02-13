from fastapi import FastAPI

from ..settings import Settings
from fastapi.middleware.cors import CORSMiddleware
from app.routes.script_launch import router as script_router

settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

app.include_router(script_router, prefix='', tags=['User'])
