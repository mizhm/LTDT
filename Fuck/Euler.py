# Kiểm tra liên thông bằng DFS
def is_connected(graph, n):
    visited = [False] * n
    stack = [0]  # Duyệt từ đỉnh đầu tiên (đỉnh 0)
    visited[0] = True

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    # Kiểm tra xem tất cả các đỉnh đều đã được thăm
    return all(visited)


# Kiểm tra xem đồ thị có phải là Eulerian hay Semi-Eulerian
def check_euler(graph):
    n = len(graph)

    # Kiểm tra liên thông
    if not is_connected(graph, n):
        return "Đồ thị không liên thông"

    # Kiểm tra bậc các đỉnh
    odd_degree_count = 0
    for node in range(n):
        if len(graph[node]) % 2 != 0:
            odd_degree_count += 1

    # Đưa ra kết quả
    if odd_degree_count == 0:
        return "Đồ thị là Euler"
    elif odd_degree_count == 2:
        return "Đồ thị là nửa Euler"
    else:
        return "Đồ thị không phải Euler hay nửa Euler"


# Ví dụ đồ thị
# Đồ thị 1 (Eulerian)
graph_eulerian = [
    [1, 3],  # Đỉnh 1 kề với đỉnh 2 và 4
    [0, 2],  # Đỉnh 2 kề với đỉnh 1 và 3
    [1, 3],  # Đỉnh 3 kề với đỉnh 2 và 4
    [0, 2]  # Đỉnh 4 kề với đỉnh 1 và 3
]

# Đồ thị 2 (Semi-Eulerian)
graph_semi_eulerian = [
    [1],  # Đỉnh 1 kề với đỉnh 2
    [0, 2],  # Đỉnh 2 kề với đỉnh 1 và 3
    [1, 3],  # Đỉnh 3 kề với đỉnh 2 và 4
    [2]  # Đỉnh 4 kề với đỉnh 3
]

# Đồ thị 3 (Không Eulerian và không Semi-Eulerian)
graph_non_eulerian = [
    [1, 2],  # Đỉnh 1 kề với đỉnh 2 và 3
    [0, 3],  # Đỉnh 2 kề với đỉnh 1 và 4
    [0, 3],  # Đỉnh 3 kề với đỉnh 1 và 4
    [1, 2, 3]  # Đỉnh 4 kề với đỉnh 1, 2 và 3
]

# Kiểm tra đồ thị
print(check_euler(graph_eulerian))  # Kết quả: Đồ thị là Eulerian
print(check_euler(graph_semi_eulerian))  # Kết quả: Đồ thị là Semi-Eulerian
print(check_euler(graph_non_eulerian))  # Kết quả: Đồ thị không phải Eulerian hoặc Semi-Eulerian
