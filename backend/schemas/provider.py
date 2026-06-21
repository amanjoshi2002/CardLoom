# schemas/provider.py

from pydantic import BaseModel


class ProviderCreate(BaseModel):
    name: str
    model: str
    api_key: str


class ProviderResponse(ProviderCreate):
    id: int

    model_config = {
        "from_attributes": True
    }