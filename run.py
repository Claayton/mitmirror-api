"""Script para rodar o programa"""
import uvicorn
from sqlalchemy_utils import database_exists, create_database
from mitmirror.infra.config.create_database import create_databases
from mitmirror.config import CONNECTION_STRING

if __name__ == "__main__":

    if not database_exists(CONNECTION_STRING):

        create_database(CONNECTION_STRING)

    create_databases()

    uvicorn.run(
        app="mitmirror.main.config.http_server_configs:create_app",
        host="0.0.0.0",
        port=6000,
        reload=True,
        debug=True,
        factory=True,
    )
