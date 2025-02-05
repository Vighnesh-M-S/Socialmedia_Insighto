from fastapi import APIRouter, HTTPException
from ..database import db

router = APIRouter()

@router.get("/posts/{username}")
async def get_posts(username: str, limit: int = 10):
    page = await db.pages.find_one({"username": username})
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")

    posts = await db.posts.find({"page_id": page["page_id"]}).limit(limit).to_list(length=limit)
    return posts
