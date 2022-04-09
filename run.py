"""Script para rodar o programa"""
import uvicorn
from mitmirror.infra.config.create_database import (
    create_database_tests,
    create_database_main,
)

if __name__ == "__main__":

    create_database_main()
    create_database_tests()

    uvicorn.run(
        app="mitmirror.main.config.http_server_configs:create_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True,
        factory=True,
    )
