def dijkstra(n, adj, start, end):
    # Khởi tạo khoảng cách từ đỉnh start
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[start] = 0
    prev = {i: None for i in range(1, n + 1)}  # Lưu lại đỉnh trước của mỗi đỉnh trong đường đi

    visited = set()

    while len(visited) < n:
        # Tìm đỉnh u có khoảng cách nhỏ nhất mà chưa được thăm
        u = -1
        min_dist = float('inf')
        for i in range(1, n + 1):
            if i not in visited and dist[i] < min_dist:
                u = i
                min_dist = dist[i]

        if u == -1:  # Không thể tiếp tục (đồ thị không liên thông)
            break

        # Đánh dấu u đã thăm
        visited.add(u)

        # Cập nhật khoảng cách đến các đỉnh kề
        for v, weight in adj[u]:
            if v not in visited and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u

    # Truy vết đường đi từ đỉnh end về đỉnh start
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()

    return dist[end], path

# Đồ thị mẫu, với các cạnh đã được gán sẵn
n = 5  # Số đỉnh
adj = {
    1: [(2, 2), (3, 4)],
    2: [(1, 2), (3, 1), (4, 7)],
    3: [(1, 4), (2, 1), (5, 3)],
    4: [(2, 7), (5, 1)],
    5: [(3, 3), (4, 1)]
}

# Nhập đỉnh xuất phát và đỉnh đích
print("Nhập đỉnh xuất phát:")
start = int(input())
print("Nhập đỉnh đích:")
end = int(input())

# Chạy thuật toán Dijkstra
shortest_distance, path = dijkstra(n, adj, start, end)

# Hiển thị kết quả
if shortest_distance == float('inf'):
    print(f"Không có đường đi từ đỉnh {start} đến đỉnh {end}.")
else:
    print(f"Đường đi ngắn nhất từ đỉnh {start} đến đỉnh {end}:")
    print(" -> ".join(map(str, path)))
    print(f"Tổng trọng số của đường đi: {shortest_distance}")
