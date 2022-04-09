"""Instanciando o app"""
from fastapi import FastAPI
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

    app.include_router(users)

    return app
