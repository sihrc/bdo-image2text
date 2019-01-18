import asyncio

from concurrent.futures import ThreadPoolExecutor

from functools import wraps

MAIN_POOL = ThreadPoolExecutor(4)


def threaded(f):
    @wraps(f)
    def wrapped(*args, _sync=False, **kwargs):
        if _sync:
            return f(*args, **kwargs)
        return asyncio.get_event_loop().run_in_executor(MAIN_POOL, f, *args, **kwargs)

    return wrapped
