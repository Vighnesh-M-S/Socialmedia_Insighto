from pydantic import BaseModel
from typing import List, Optional

class Page(BaseModel):
    username: str
    page_name: str
    page_url: str
    page_id: str
    profile_pic: Optional[str]
    email: Optional[str]
    website: Optional[str]
    category: Optional[str]
    followers: int
    likes: int
    creation_date: Optional[str]

class Post(BaseModel):
    page_id: str
    post_id: str
    content: str
    likes: int
    comments: List[str]