import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def scrape_facebook_page(username: str):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Page not found")

    soup = BeautifulSoup(response.text, 'html.parser')
    page_name = soup.title.string if soup.title else "Unknown"
    page_id = username  # Simplified

    return {
        "username": username,
        "page_name": page_name,
        "page_url": url,
        "page_id": page_id,
        "followers": 1000,
        "likes": 500
    }