from pydantic import BaseModel


class CustomBaseModel(BaseModel):

    def model_dump(self, *args, **kwargs):
        md: dict = super().model_dump(*args, **kwargs)
        return {k: v for k, v in md.items() if v is not None}
