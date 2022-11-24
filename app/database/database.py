from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from app.config import settings

db_user: str = settings.db_user
db_password: str = settings.db_password
db_host: str = settings.db_host
db_port: str = settings.db_port
db_database: str = settings.db_database

db_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"

print("database string:", db_string)

engine = create_engine(db_string, echo=True, future=True)
if not database_exists(engine.url):
    create_database(engine.url)
