from fastapi import APIRouter


router = APIRouter()


@router.post("")
async def quotes():
    return


@router.get("/{id}")
async def quote(id: int):
    return
