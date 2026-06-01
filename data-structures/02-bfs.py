from collections import deque

def bfs(graph, start):
    visited = set ()
    visited.add(start)
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print("Removed node : {}".format(node))
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

print(bfs(graph, "A"))