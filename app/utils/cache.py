from .database import redis

async def get_cache(key: str):
    return await redis.get(key)

async def set_cache(key: str, value: str, ttl: int = 300):
    await redis.set(key, value, ex=ttl)