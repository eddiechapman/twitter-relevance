import os
import pathlib
from dotenv import load_dotenv

basedir = pathlib.Path(__file__).parent.resolve()
load_dotenv()


class Config:
    DEBUG = False
    UPLOAD_EXTENSIONS = ["csv"]
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(basedir / "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADS = basedir / "uploads"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "").replace("postgres://", "postgresql://")


class DevelopmentConfig(Config):
    SECRET_KEY = "very secret"
    DEBUG = True
