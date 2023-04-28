import heapq
import math


def shortest_path(graph, start, goal):

    open_set = [(0, 0, start, [])]
    closed_set = set()

    while open_set:
        priority, g_cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(path, current)

        if current not in closed_set:
            closed_set.add(current)

            for neighbor in get_neighbors(current, graph.roads):
                if neighbor not in closed_set:
                    g = g_cost + \
                        heuristic(current, neighbor, graph.intersections)
                    f = g + heuristic(neighbor, goal, graph.intersections)
                    heapq.heappush(open_set, (f, g, neighbor,
                                   reconstruct_path(path, current)))

    return []  # No path found


def reconstruct_path(path, current):
    return path + [current]


def heuristic(node1, node2, intersections):
    return euclidean_distance(node1, node2, intersections)


def euclidean_distance(node1, node2, intersections):
    x1, y1 = intersections[node1]
    x2, y2 = intersections[node2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_neighbors(node, roads):
    return roads[node]


# references:
# A* (A Star) Search Algorithm - Computerphile: https://www.youtube.com/watch?v=ySN5Wnu88nE
# A* Search Algorithm: https://www.geeksforgeeks.org/a-search-algorithm/
