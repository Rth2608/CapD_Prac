from fastapi import FastAPI
from app import routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router, prefix, tags in routers.all_routers:
    app.include_router(router, prefix=prefix, tags=tags)
