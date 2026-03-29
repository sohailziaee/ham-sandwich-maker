from pydantic import BaseModel

class SandwichBase(BaseModel):
    name: str
    description: str

class SandwichCreate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int
    class Config:
        from_attributes = True

class ResourceBase(BaseModel):
    name: str
    quantity: int

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    class Config:
        from_attributes = True

class RecipeBase(BaseModel):
    sandwich_id: int
    instructions: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_name: str
    description: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    class Config:
        from_attributes = True

class OrderDetailBase(BaseModel):
    order_id: int
    sandwich_id: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetail(OrderDetailBase):
    id: int
    class Config:
        from_attributes = True