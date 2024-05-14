from fastapi import Depends
from app.core.database import Session
from fastapi.security import OAuth2PasswordBearer
from app.core.configs import settings
from app.usecases.user_usecases import UserUseCases
from sqlalchemy.orm import Session as SqlAchemySession

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


def auth(
    db_session: SqlAchemySession = Depends(get_db_session),
    token=Depends(oauth_scheme),
):
    if settings.TEST_MODE:
        return

    uc = UserUseCases(db_session=db_session)
    uc.verify_token(token=token)
