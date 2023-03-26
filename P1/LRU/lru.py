#
'''
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set()
is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache,
it is known as a cache hit. If, however, the entry is not found,
it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache.
 If the cache is full and we want to add a new entry to the cache,
 we use some criteria to remove an element. After removing an element,
 we use the put() operation to insert the new element.
   The remove operation should also be fast.

For our first problem,
the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry
when the cache memory reaches its limit. For the current problem,
consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element.
If the cache is full, you must write code that removes
the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.
'''


class LRU_Cache(object):

    def __init__(self, capacity):
        self.oldest_item_tracker = []
        self.cache = {}
        self.capacity = capacity
        self.entries = 0

    def get(self, key):

        if key in self.cache and self.cache[key]:
            self.update_recency(key)
            return self.cache[key]

        return -1

    def update_recency(self, key):

        if key in self.oldest_item_tracker:
            self.oldest_item_tracker.remove(key)
        self.oldest_item_tracker.append(key)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.cache:
            self.cache[key] = value
            self.update_recency(key)

            if (self.reached_capacity() == False):
                self.entries += 1
            else:
                self.remove_oldest()
                self.cache[key] = value

    def reached_capacity(self):
        return self.entries == self.capacity

    def remove_oldest(self):
        oldest_item = self.oldest_item_tracker[0]
        self.cache[oldest_item] = None

    def is_recent(self, key):

        if (self.reached_capacity() == False):
            return True

        return key != self.oldest_item_tracker[0]
