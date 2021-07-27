from fastapi import FastAPI

from .routes import urls

app = FastAPI(title="URL Shortener", version="1.0.0", docs_url="/docs")

app.include_router(urls.router)
