from fastapi import APIRouter


router = APIRouter()


@router.post("")
async def application():
    return


@router.get("/{id}")
async def application(id: int):
    return
