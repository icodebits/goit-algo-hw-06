# Алгоритм DFS (пошук в глибину)
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                stack.append((next_vertex, path + [next_vertex]))

# Алгоритм BFS (пошук в ширину)
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))
