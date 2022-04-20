"""Instanciando o app"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..routes import users


def create_app() -> FastAPI:
    """Funcao de criaçao do app"""

    app = FastAPI(
        title="MitMirrorApi",
        version="0.0.1",
        description="""
        Backend do MitMirror.
        """,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(users)

    return app
