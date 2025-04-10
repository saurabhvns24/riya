from fastapi import APIRouter

router = APIRouter(prefix="/metal", tags=["Metal"])

@router.get("/price")
def get_price():
    # Placeholder, you can integrate any real API or set your logic
    return {
        "gold_per_gram": 6500,
        "silver_per_gram": 75
    }