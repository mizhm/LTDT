def floyd_warshall(n, adj):
    # Khởi tạo ma trận khoảng cách
    dist = [[float('inf')] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]  # Để truy vết đường đi

    # Đặt khoảng cách giữa các đỉnh kề là trọng số của các cạnh
    for u in adj:
        for v, weight in adj[u]:
            dist[u-1][v-1] = weight
            next_node[u-1][v-1] = v

    # Đặt khoảng cách từ đỉnh đến chính nó bằng 0
    for i in range(n):
        dist[i][i] = 0

    # Dùng thuật toán Floyd-Warshall để tính tất cả các cặp đường đi ngắn nhất
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

def reconstruct_path(next_node, start, end):
    # Truy vết đường đi từ đỉnh start đến đỉnh end
    path = []
    if next_node[start][end] is None:
        return path
    current = start
    while current != end:
        path.append(current + 1)
        current = next_node[current][end] - 1
    path.append(end + 1)
    return path

# Đồ thị mẫu, với các cạnh đã được gán sẵn
n = 5  # Số đỉnh
adj = {
    1: [(2, 2), (3, 4)],
    2: [(1, 2), (3, 1), (4, 7)],
    3: [(1, 4), (2, 1), (5, 3)],
    4: [(2, 7), (5, 1)],
    5: [(3, 3), (4, 1)]
}

# Chạy thuật toán Floyd-Warshall
dist, next_node = floyd_warshall(n, adj)

# Nhập đỉnh xuất phát và đỉnh đích
print("Nhập đỉnh xuất phát:")
start = int(input()) - 1  # Chuyển sang chỉ số bắt đầu từ 0
print("Nhập đỉnh đích:")
end = int(input()) - 1    # Chuyển sang chỉ số bắt đầu từ 0

# Kết quả
if dist[start][end] == float('inf'):
    print(f"Không có đường đi từ đỉnh {start+1} đến đỉnh {end+1}.")
else:
    path = reconstruct_path(next_node, start, end)
    print(f"Đường đi ngắn nhất từ đỉnh {start+1} đến đỉnh {end+1}:")
    print(" -> ".join(map(str, path)))
    print(f"Tổng trọng số của đường đi: {dist[start][end]}")
