from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from iq_air.router import router as iq_air_router

app = FastAPI(
    title="Air condition status API",
    description="REST API for retrieving information about current air conditions",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

app.include_router(iq_air_router)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
