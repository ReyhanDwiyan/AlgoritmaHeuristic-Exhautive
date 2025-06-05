from collections import deque

graph = {
    0: [1, 2, 3],
    1: [4],
    2: [1],
    3: [4, 5],
    4: [5],
    5: [2]
}

# BFS
def bfs(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result

# DFS (rekursif)
def dfs(start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited, result)

    return result

# Uji dari node 0
print("Hasil BFS dari simpul 0:", bfs(0))
print("Hasil DFS dari simpul 0:", dfs(0))
