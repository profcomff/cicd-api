import uvicorn

from app.routes.base import app


if __name__ == '__main__':
    uvicorn.run(app)
