from typing import Any, Dict

from fastapi import FastAPI

from iq_air.router import router as iq_air_router

app = FastAPI(
    title="Air condition status API",
    description="REST API for retrieving information about current air conditions",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

app.include_router(iq_air_router)
