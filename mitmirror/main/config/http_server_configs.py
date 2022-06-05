"""Instanciando o app"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from ..routes import users, auth


def create_app() -> FastAPI:
    """Funcao de criaçao do app"""

    app = FastAPI(
        title="MitMirrorApi",
        version="0.0.1",
        description="""Backend para o MitMirror""",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(users)
    app.include_router(auth)

    @app.get("/")
    def root():
        """Rota raiz"""
        return RedirectResponse("/docs")

    return app
