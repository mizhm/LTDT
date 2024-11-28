graph = {
    1: [{2: 33}, {3: 17}],
    2: [{1: 33}, {3: 18}, {4: 20}],
    3: [{1: 17}, {2: 18}, {4: 16}, {5: 4}],
    4: [{2: 20}, {3: 16}, {5: 9}, {6: 8}],
    5: [{3: 4}, {4: 9}, {6: 14}],
    6: [{4: 8}, {5: 14}]
}


def bfs():
    queue = [1]
    visited = []
    while queue and len(visited) != len(graph.keys()):
        visited.append(queue.pop(0))
        queue = [list(item.keys())[0] for item in
                 list(sorted(graph[visited[-1]], key=lambda x: list(x.values())[0])) if
                 list(item.keys())[0] not in visited and list(item.keys())[0] not in queue]
    print(visited)


if __name__ == '__main__':
    bfs()
