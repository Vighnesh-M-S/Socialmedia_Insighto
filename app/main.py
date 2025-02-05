from fastapi import FastAPI
from .routes import page_routes, post_routes

app = FastAPI()

app.include_router(page_routes.router)
app.include_router(post_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)