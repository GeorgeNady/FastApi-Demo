import gzip
from typing import Callable, List

from fastapi import Body, FastAPI, Request, Response

from src.routes import users_routes
from src.routes import visits_routes

app = FastAPI(
    debug=True,
    swagger_ui_parameters={
        "syntaxHighlight": False,
        "dom_id": "#swagger-ui",
        "layout": "BaseLayout",
        "deepLinking": True,
        "showExtensions": True,
        "showCommonExtensions": True,
    },
)

app.include_router(users_routes.router)
app.include_router(visits_routes.router)