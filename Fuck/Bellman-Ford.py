def bellman_ford(n, edges, start, end):
    # Khởi tạo khoảng cách từ đỉnh start
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[start] = 0

    # Thực hiện V-1 lần lặp (V là số đỉnh)
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Kiểm tra chu trình âm
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("Đồ thị có chu trình âm.")
            return None, None

    # Truy vết đường đi từ đỉnh end về đỉnh start
    path = []
    current = end
    while current != start:
        path.append(current)
        # Tìm đỉnh trước của current
        for u, v, weight in edges:
            if dist[current] == dist[u] + weight:
                current = u
                break
    path.append(start)
    path.reverse()

    return dist[end], path

# Đồ thị mẫu, với các cạnh đã được gán sẵn
n = 5  # Số đỉnh
edges = [
    (1, 2, 2),
    (1, 3, 4),
    (2, 3, 1),
    (2, 4, 7),
    (3, 5, 3),
    (4, 5, 1)
]

# Nhập đỉnh xuất phát và đỉnh đích
print("Nhập đỉnh xuất phát:")
start = int(input())
print("Nhập đỉnh đích:")
end = int(input())

# Chạy thuật toán Bellman-Ford
shortest_distance, path = bellman_ford(n, edges, start, end)

# Hiển thị kết quả
if shortest_distance is None:
    print("Không thể tìm đường đi do chu trình âm.")
else:
    print(f"Đường đi ngắn nhất từ đỉnh {start} đến đỉnh {end}:")
    print(" -> ".join(map(str, path)))
    print(f"Tổng trọng số của đường đi: {shortest_distance}")
