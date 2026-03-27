from fastapi import FastAPI
from .api import datasets_routes, lineage_routes, search_routes

app = FastAPI(title="Metadata Management System")

app.include_router(datasets_routes.router)
app.include_router(lineage_routes.router)
app.include_router(search_routes.router)


