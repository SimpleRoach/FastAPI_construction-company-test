from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    category_id: int
    price: float
    description: str


class ProductCreate(ProductBase):
    pass


class Product (ProductBase):
    id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category (CategoryBase):
    id: int
    products : list[Product] = []

    class Config:
        orm_mode = True