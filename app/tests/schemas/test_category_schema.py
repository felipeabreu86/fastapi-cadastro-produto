import pytest
from app.schemas.category import Category


def test_category_schema():
    category = Category(name="Roupa", slug="roupa")
    assert category.model_dump() == {"name": "Roupa", "slug": "roupa"}


def test_category_schema_invalid_slug():
    for invalid_value in ("roupa de cama", "cão", "Roupa"):
        with pytest.raises(ValueError):
            Category(name="Roupa", slug=invalid_value)
