def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


graph = {
    '1': ['2', '3'],
    '2': ['1', '3'],
    '3': ['1', '2','4','5'],
    '4': ['3','5','7'],
    '5': ['3', '4','6'],
    '6': ['5'],
    '7': ['4']
}

print("DFS từ đỉnh 1")
dfs(graph, '1')
