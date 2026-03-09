from fastapi import APIRouter

router = APIRouter()

todos = []

@router.get("/todos")
def get_todos():
    return todos