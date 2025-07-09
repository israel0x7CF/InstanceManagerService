from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/test"
)


class TestModel(BaseModel):
    pass
@router.post("/")
async def create_test_item():
    pass