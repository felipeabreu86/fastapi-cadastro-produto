from sqlalchemy import Column, Integer, String
from app.core.configs import settings
from sqlalchemy.orm import relationship


class Category(settings.DB_BASE_MODEL):
    __tablename__ = "categories"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    slug = Column("slug", String, nullable=False)
    products = relationship("Product", back_populates="category")


### ----------------------------------------------------------------------------

## Migrations com Alembic

# Rodar comando no container:
# docker-compose run --user 1000 app sh -c 'alembic init migrations'
# docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add comment here"'
# docker-compose run --user 1000 app sh -c 'alembic upgrade head'
