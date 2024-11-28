graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 6],
    6: [4, 5]
}


def bfs():
    queue = [1]
    visited = []
    while queue and len(visited) != len(graph.keys()):
        visited.append(queue.pop(0))
        queue = queue + [item for item in list(graph[visited[-1]]) if item not in visited and item not in queue]
    print(visited)


if __name__ == '__main__':
    bfs()
