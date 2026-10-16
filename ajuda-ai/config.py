import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY="minha_chave_secreta_ajuda-ai"
    SQLALCHEMY_DATABASE_URI="sqlite:///ajuda_ai.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    