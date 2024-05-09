from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    slug = Column("slug", String, nullable=False)


### ----------------------------------------------------------------------------

## Migrations com Alembic

# Rodar comando no container:
# docker-compose run --user 1000 app sh -c 'alembic init migrations'
# docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add categories table"'
# docker-compose run --user 1000 app sh -c 'alembic upgrade head'
