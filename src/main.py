from fastapi import FastAPI
import uvicorn

from product.router import router as product_router
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
app = FastAPI()

app.include_router(product_router, prefix="/product", tags=["product"])


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
