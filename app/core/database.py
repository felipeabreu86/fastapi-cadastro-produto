from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from app.core.configs import settings


engine: Engine = create_engine(
    settings.DB_URL,
    pool_pre_ping=True,
)

Session = sessionmaker(
    bind=engine,
)
