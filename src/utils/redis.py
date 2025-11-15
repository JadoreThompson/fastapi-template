from redis import Redis
from redis.asyncio import Redis as AsyncRedis

from config import REDIS_DB, REDIS_HOST, REDIS_PORT


kw = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "db": REDIS_DB,
    "encoding": "utf-8",
    "decode_responses": True,
}
REDIS_CLIENT = AsyncRedis(**kw)
REDIS_CLIENT_SYNC = Redis(**kw)
del kw
