from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.routers import core, quotes, applications
from app.schemas.core import APIResponse, ErrorDetail

app = FastAPI()

app.include_router(core.router)
app.include_router(quotes.router, prefix="/quotes")
app.include_router(applications.router, prefix="/applications")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    return JSONResponse(
        status_code=exception.status_code,
        content=APIResponse(
            success=False,
            error=ErrorDetail(code=exception.status_code,
                              message=exception.detail),
        ).dict()
    )
