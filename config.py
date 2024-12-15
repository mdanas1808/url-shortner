import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://url_admin:ABCD%401234@localhost/url_shortener")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

