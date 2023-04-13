class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)

    def insert(self, resources, handler):
        node = self.root
        for resource in resources:
            node.insert(resource, handler)
            node = node.children[resource]
        node.handler = handler

    def find(self, resources):
        node = self.root
        for resource in resources:
            if resource not in node.children:
                return None
            node = node.children[resource]
        return node.handler if node.handler is not None else None


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, resource, handler):

        if resource not in self.children:
            self.children[resource] = RouteTrieNode(handler)


class Router:
    def __init__(self, handler, not_found_handler):
        self.trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, resource, handler):
        resources = self.split_resource(resource)
        self.trie.insert(resources, handler)

    def lookup(self, resource):
        resources = self.split_resource(resource)
        handler = self.trie.find(resources)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_resource(self, resource):
        resources = resource.split("/")
        resources = [resource for resource in resources if resource != ""]
        return resources


# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home", "home handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))
# root handler

print(router.lookup("/home"))
# 'home handler
print(router.lookup("/home/about"))
# 'about handler'
print(router.lookup("/home/about/"))
# 'about handler'
print(router.lookup("/home/about/me"))
# 'not found handler'
