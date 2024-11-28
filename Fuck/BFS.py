def bfs(graph, start):
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    '1': ['2', '3'],
    '2': ['1', '3'],
    '3': ['1', '2','4','5'],
    '4': ['3','5','7'],
    '5': ['3', '4','6'],
    '6': ['5'],
    '7': ['4']
}

print("BFS từ đỉnh 1:")
bfs(graph, '1')
