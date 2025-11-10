from fastapi import APIRouter

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.get("/")
def list_datasets():
    return []