"""Script para rodar o programa"""
import uvicorn
from sqlalchemy_utils import database_exists, create_database
from mitmirror.infra.config.create_database import create_db
from mitmirror.config import settings

if __name__ == "__main__":

    if not database_exists(settings.CONNECTION_STRING):

        create_database(settings.CONNECTION_STRING)

    create_db()

    uvicorn.run(
        app="mitmirror.main.config.http_server_configs:create_app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        debug=True,
        factory=True,
    )
