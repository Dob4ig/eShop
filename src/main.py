from fastapi import FastAPI
import uvicorn

from product.router import router as product_router


app = FastAPI()

app.include_router(product_router, prefix="/product", tags=["product"])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
