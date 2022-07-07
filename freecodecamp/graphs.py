# To work with graphs we will craete adjency lists
# It is basically a lists of particular node with their neighbours

# Creating a graph as an adjency list?
class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            # insert into the right lists
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, v) for n, v in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


class Graph_v2():
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self) -> str:
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result


# Breadth First Search: For each node we will find out how far away it is from the source and that will
# be the shortest path between the two, in simple words finding the shortest path between two points
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True
    queue.append(root)
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1

        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1+distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent


# Depth First Search: Getting the shortest path usign Stack almost same to BFS
def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result


# We can get the shortest path using BFS but whenerver we are asked to get the shortest path
# in weighted graphs use shortest paths algorithm (Dijkstra's Algorithm)

def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        # update the distacnes of all the nieghtbous
        update_distances(graph, current, distance)

        # find the 1st unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
        visited[current] = True

    return distance[target]


def update_distances(graph, current, distance, parent=None):
    neighbours = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbours):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    # Pick the next unvisited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

# graph1 = Graph(5, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
# print(dfs(graph1, 3))


# graph2 = Graph_v2(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4),
#                   (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)], weighted=True)
# print(graph2.__repr__())

graph3 = Graph_v2(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5),
                  (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)], True, True)
# print(graph3.__repr__())
print(shortest_path(graph3, 0, 5))
