from sqlalchemy import create_engine

from app.config import settings

db_user: str = settings.db_user
db_password: str = settings.db_password
db_host: str = settings.db_host
db_port: str = settings.db_port
db_database: str = settings.db_database

db_string = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
