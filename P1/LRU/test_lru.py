from lru import LRU_Cache


cache = LRU_Cache(5)
cache.set(1, "Hello")

print(cache.get(1))
# Hello


lru = LRU_Cache(5)
lru.set(1, "1")
lru.set(2, "2")
lru.set(3, "3")
lru.set(4, "4")
lru.set(5, "5")
lru.get(2)
lru.get(3)
lru.get(4)
lru.get(5)
lru.get(6)
lru.get(1)
lru.set(6, "6")

print(lru.is_recent(1))
# TRUE
print(lru.get(2))
# -1


cache = LRU_Cache(5)
cache.set(1, "1")
cache.set(1, "1")
print(cache.entries)
#  1


cache = LRU_Cache(5)
cache.set(1, "1")
cache.set(1, "1")
print(cache.is_recent(1))
# TRUE
