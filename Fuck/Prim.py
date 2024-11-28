def prim(n, edges):
    # Xây dựng danh sách kề từ danh sách cạnh
    adj = {i: [] for i in range(1, n + 1)}
    for u, v, c in edges:
        adj[u].append((v, c))
        adj[v].append((u, c))

    # Khởi tạo
    visited = set()
    total_weight = 0
    mst_edges = []  # Danh sách các cạnh trong cây khung nhỏ nhất

    # Bắt đầu từ đỉnh 1 (hoặc bất kỳ đỉnh nào)
    visited.add(1)
    available_edges = adj[1]  # Các cạnh khả dụng từ đỉnh 1

    while len(visited) < n:
        # Tìm cạnh có trọng số nhỏ nhất trong các cạnh khả dụng
        min_edge = None
        for v, c in available_edges:
            if v not in visited and (min_edge is None or c < min_edge[1]):
                min_edge = (v, c)

        # Thêm cạnh này vào MST
        if min_edge is None:
            break  # Đồ thị không liên thông
        v, c = min_edge
        total_weight += c
        mst_edges.append((v, c))
        visited.add(v)

        # Cập nhật các cạnh khả dụng
        for neighbor, weight in adj[v]:
            if neighbor not in visited:
                available_edges.append((neighbor, weight))

        # Loại bỏ các cạnh dẫn đến các đỉnh đã thăm
        available_edges = [(v, c) for v, c in available_edges if v not in visited]

    return total_weight, mst_edges

# Ví dụ input
n = 4
edges = [
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 3),
    (4, 1, 4)
]

# Tìm cây khung nhỏ nhất
total_weight, mst_edges = prim(n, edges)
print("Tổng trọng số:", total_weight)
print("Các cạnh trong cây khung nhỏ nhất:", mst_edges)
