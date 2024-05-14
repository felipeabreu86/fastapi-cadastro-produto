from sqlalchemy import Column, Integer, String
from app.core.configs import settings


class User(settings.DB_BASE_MODEL):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)


### ----------------------------------------------------------------------------

## Migrations com Alembic

# Rodar comando no container:
# docker-compose run --user 1000 app sh -c 'alembic init migrations'
# docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add comment here"'
# docker-compose run --user 1000 app sh -c 'alembic upgrade head'
