from motor.motor_asyncio import AsyncIOMotorClient
import aioredis
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

# MongoDB Setup
client = AsyncIOMotorClient(MONGO_URI)
db = client.facebook_insights

# Redis Setup
redis = aioredis.from_url(REDIS_URL)
