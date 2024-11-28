graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 6],
    6: [4, 5]
}


def dfs():
    stack = [6]
    visited = []
    while stack and len(visited) != len(graph.keys()):
        visited.append(stack.pop(0))
        stack = [item for item in list(sorted(graph[visited[-1]])) if item not in visited] + stack
    print(visited)


if __name__ == '__main__':
    dfs()
