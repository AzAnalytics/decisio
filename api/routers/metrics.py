from fastapi import APIRouter

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("/overview")
def overview():
    return {"message": "overview metrics (à implémenter)"}