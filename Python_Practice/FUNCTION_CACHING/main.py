from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(4)
    return n*5

print(fx(20))
print(fx(2))
print(fx(3))

print(fx(20))
print(fx(2))
print(fx(21))
