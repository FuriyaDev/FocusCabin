from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth_router

app = FastAPI(title="API", version="1.0.0", description="API for the cabines")

app.include_router(auth_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)