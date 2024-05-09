from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session
from app.core.deps import get_db_session
from app.schemas.category import Category, CategoryOutput
from app.usecases.category_usecases import CategoryUseCases


router = APIRouter(prefix="/category", tags=["Category"])


@router.post(
    "/add",
    status_code=status.HTTP_201_CREATED,
    description="Add new category",
)
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session),
):
    CategoryUseCases(db_session).add_category(category)
    return Response(status_code=status.HTTP_201_CREATED)


@router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    description="List categories",
)
def list_categories(db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    return uc.list_categories()
