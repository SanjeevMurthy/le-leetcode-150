

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print("Added node : {}".format(node))

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

# Stack based implementation
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print("Popped node : {}".format(node))
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

print(dfs(graph, "A"))
print(dfs_iterative(graph, "A"))