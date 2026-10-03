from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    price: float = Field(ge=0, description="Price must be greater than or equal to 0")
    category: str
    description: str


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float = Field(ge=0, description="Price must be greater than or equal to 0")
    category: str
    description: str


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = Field(
        default=None, ge=0, description="Price must be greater than or equal to 0"
    )
    category: str | None = None
    description: str | None = None
