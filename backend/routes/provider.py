#all routes for provider
from fastapi import HTTPException
from fastapi import APIRouter,Depends

from schemas.provider import ProviderCreate
from models.provider import Provider
from utils.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter()



router = APIRouter(
    prefix="/api/providers",
    tags=["Providers"]
)


@router.post("/")
def create_provider(provider: ProviderCreate, db: Session = Depends(get_db)):
    db_provider = Provider(name=provider.name, model=provider.model, api_key=provider.api_key)
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return {"message": "Provider created successfully", "provider": db_provider}





@router.get("/")
def get_providers(db: Session = Depends(get_db)):
    providers = db.query(Provider).all()
    return providers

@router.delete("/{provider_id}")
def delete_provider(provider_id: int, db: Session = Depends(get_db)):
    provider = (
        db.query(Provider)
        .filter(Provider.id == provider_id)
        .first()
    )

    if provider is None:
        return {"message": "Provider not found"}

    db.delete(provider)
    db.commit()

    return {"message": "Provider deleted successfully"}





@router.put("/{provider_id}")
def update_provider(
    provider_id: int,
    provider: ProviderCreate,
    db: Session = Depends(get_db)
):
    db_provider = (
        db.query(Provider)
        .filter(Provider.id == provider_id)
        .first()
    )

    if db_provider is None:
        raise HTTPException(status_code=404, detail="Provider not found")

    db_provider.name = provider.name
    db_provider.model = provider.model
    db_provider.api_key = provider.api_key

    db.commit()
    db.refresh(db_provider)

    return {
        "message": "Provider updated successfully",
        "provider": db_provider
    }