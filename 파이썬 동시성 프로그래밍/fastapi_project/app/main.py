from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.book import BookModel

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword='파이썬', publisher='BJPublic', price=1200, image='me.png')
    await mongodb.engine.save(book) # DB에 저장
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "taxijjang"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "taxijjang", "keyword": q}
    )


@app.on_event('startup')
def on_app_start():
    """before app starts"""
    print("start server")
    mongodb.connect()


@app.on_event('shutdown')
def on_app_shutdown():
    """after app shutdown"""
    print("by server")
    mongodb.close()
