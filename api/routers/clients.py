from fastapi import APIRouter

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/")
def list_clients():
    return []