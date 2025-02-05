from fastapi import APIRouter, HTTPException
from ..database import db
from ..scraper import scrape_facebook_page
from ..utils.cache import get_cache, set_cache

router = APIRouter()

@router.post("/scrape/{username}")
async def scrape_and_store(username: str):
    cached_page = await get_cache(username)
    if cached_page:
        return cached_page

    page_data = scrape_facebook_page(username)
    await db.pages.insert_one(page_data)
    await set_cache(username, str(page_data))
    return page_data

@router.get("/page/{username}")
async def get_page(username: str):
    page = await db.pages.find_one({"username": username})
    if page:
        return page
    return await scrape_and_store(username)