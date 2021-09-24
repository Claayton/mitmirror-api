from flask_cors import CORS

cross = CORS()

def init_app(app):
    cross.init_app(app)
    
# A principio isso só é requirido para rodar a aplicação em server local
