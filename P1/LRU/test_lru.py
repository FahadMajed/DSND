from lru import LRU_Cache


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1


def test_should_add_entry():
    cache = LRU_Cache(5)
    cache.set(1, "Hello")

    assert (cache.get(1) == "Hello")


# Test Case 2


def test_should_remove_the_least_recently_used():
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
    print(lru.cache)
    assert (lru.is_recent(1))
    assert (lru.get(2) == -1)


# Test Case 3

def test_should_not_add_key_twice():
    cache = LRU_Cache(5)
    cache.set(1, "1")
    cache.set(1, "1")
    assert (cache.entries == 1)

# Test Case 4


def test_update_recency():
    cache = LRU_Cache(5)
    cache.set(1, "1")
    cache.set(1, "1")

    assert (cache.is_recent(1))
