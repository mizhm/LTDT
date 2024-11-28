# Hàm nhập đồ thị từ danh sách đỉnh kề
def input_adj_list():
    # Nhập số lượng đỉnh và cạnh
    n = int(input("Nhập số lượng đỉnh n: "))
    adj_list = []

    print(f"Nhập danh sách đỉnh kề:")
    for i in range(n):
        adj_list.append(list(map(int, input(f"Đỉnh {i + 1}: ").split())))

    return n, adj_list


# Chuyển từ danh sách đỉnh kề sang danh sách cạnh kề
def convert_to_edge_list_from_adj_list(n, adj_list):
    edges = []

    for i in range(n):
        for v in adj_list[i]:
            if i < v - 1:  # Chỉ lấy cạnh u-v một lần (vì đồ thị vô hướng)
                edges.append((i + 1, v))  # Lưu các cạnh u-v

    return edges


# Chuyển từ danh sách đỉnh kề sang ma trận kề
def convert_to_matrix_from_adj_list(n, adj_list):
    matrix = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in adj_list[u]:
            matrix[u][v - 1] = 1  # Chuyển từ chỉ số 1 sang chỉ số 0
            matrix[v - 1][u] = 1  # Đồ thị vô hướng nên cần cập nhật cả hai chiều

    return matrix


# Chuyển từ danh sách đỉnh kề sang ma trận cạnh kề
def convert_to_edge_matrix_from_adj_list(n, adj_list):
    edge_matrix = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in adj_list[u]:
            edge_matrix[u][v - 1] = 1  # Cạnh nối giữa u và v
            edge_matrix[v - 1][u] = 1  # Cạnh nối giữa v và u (đồ thị vô hướng)

    return edge_matrix


# Chuyển từ ma trận kề sang danh sách cạnh kề
def convert_to_edge_list_from_matrix(n, matrix):
    edges = []

    for u in range(n):
        for v in range(u + 1, n):  # Chỉ lấy cạnh u-v một lần
            if matrix[u][v] == 1:
                edges.append((u + 1, v + 1))  # Chuyển chỉ số từ 0 -> 1

    return edges


# Chuyển từ ma trận kề sang danh sách đỉnh kề
def convert_to_adj_list_from_matrix(n, matrix):
    adj_list = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if matrix[u][v] == 1:
                adj_list[u].append(v + 1)  # Chuyển chỉ số từ 0 -> 1

    return adj_list


# Chuyển từ ma trận kề sang ma trận cạnh kề
def convert_to_edge_matrix_from_matrix(n, matrix):
    edge_matrix = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if matrix[u][v] == 1:
                edge_matrix[u][v] = 1  # Đặt 1 ở các vị trí có cạnh
                edge_matrix[v][u] = 1  # Đồ thị vô hướng

    return edge_matrix


# Chuyển từ ma trận cạnh kề sang danh sách cạnh kề
def convert_to_edge_list_from_edge_matrix(n, edge_matrix):
    edges = []

    for u in range(n):
        for v in range(u + 1, n):  # Chỉ lấy cạnh u-v một lần
            if edge_matrix[u][v] == 1:
                edges.append((u + 1, v + 1))  # Chuyển chỉ số từ 0 -> 1

    return edges


# Chuyển từ ma trận cạnh kề sang danh sách đỉnh kề
def convert_to_adj_list_from_edge_matrix(n, edge_matrix):
    adj_list = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if edge_matrix[u][v] == 1:
                adj_list[u].append(v + 1)  # Chuyển chỉ số từ 0 -> 1

    return adj_list


# Chuyển từ ma trận cạnh kề sang ma trận kề
def convert_to_matrix_from_edge_matrix(n, edge_matrix):
    matrix = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if edge_matrix[u][v] == 1:
                matrix[u][v] = 1
                matrix[v][u] = 1  # Đồ thị vô hướng

    return matrix


# Nhập thông tin đồ thị từ danh sách đỉnh kề
n, adj_list = input_adj_list()

# Chuyển từ danh sách đỉnh kề sang các dạng khác
edges_from_adj_list = convert_to_edge_list_from_adj_list(n, adj_list)
matrix_from_adj_list = convert_to_matrix_from_adj_list(n, adj_list)
edge_matrix_from_adj_list = convert_to_edge_matrix_from_adj_list(n, adj_list)

# Xuất kết quả từ danh sách đỉnh kề
print("\nDanh sách cạnh kề từ danh sách đỉnh kề:")
print(edges_from_adj_list)

print("\nMa trận kề từ danh sách đỉnh kề:")
for row in matrix_from_adj_list:
    print(" ".join(map(str, row)))

print("\nMa trận cạnh kề từ danh sách đỉnh kề:")
for row in edge_matrix_from_adj_list:
    print(" ".join(map(str, row)))

# Nhập ma trận kề
n = int(input("Nhập số lượng đỉnh n: "))
matrix = []
print("Nhập ma trận kề:")
for i in range(n):
    matrix.append(list(map(int, input().split())))

# Chuyển từ ma trận kề sang các dạng khác
edges_from_matrix = convert_to_edge_list_from_matrix(n, matrix)
adj_list_from_matrix = convert_to_adj_list_from_matrix(n, matrix)
edge_matrix_from_matrix = convert_to_edge_matrix_from_matrix(n, matrix)

# Xuất kết quả từ ma trận kề
print("\nDanh sách cạnh kề từ ma trận kề:")
print(edges_from_matrix)

print("\nDanh sách đỉnh kề từ ma trận kề:")
for i in range(n):
    print(f"{i + 1}: {adj_list_from_matrix[i]}")

print("\nMa trận cạnh kề từ ma trận kề:")
for row in edge_matrix_from_matrix:
    print(" ".join(map(str, row)))

# Nhập ma trận cạnh kề
edge_matrix = []
print("Nhập ma trận cạnh kề:")
for i in range(n):
    edge_matrix.append(list(map(int, input().split())))

# Chuyển từ ma trận cạnh kề sang các dạng khác
edges_from_edge_matrix = convert_to_edge_list_from_edge_matrix(n, edge_matrix)
adj_list_from_edge_matrix = convert_to_adj_list_from_edge_matrix(n, edge_matrix)
matrix_from_edge_matrix = convert_to_matrix_from_edge_matrix(n, edge_matrix)

# Xuất kết quả từ ma trận cạnh kề
print("\nDanh sách cạnh kề từ ma trận cạnh kề:")
print(edges_from_edge_matrix)

print("\nDanh sách đỉnh kề từ ma trận cạnh kề:")
for i in range(n):
    print(f"{i + 1}: {adj_list_from_edge_matrix[i]}")

print("\nMa trận kề từ ma trận cạnh kề:")
for row in matrix_from_edge_matrix:
    print(" ".join(map(str, row)))
