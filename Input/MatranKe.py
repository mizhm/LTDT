"""
input:
5
0 1 1 1 0
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
0 1 1 1 0
"""



# Hàm nhập đồ thị từ ma trận kề
def input_matrix():
    # Nhập số lượng đỉnh n
    n = int(input("Nhập số lượng đỉnh n: "))
    matrix = []

    print("Nhập ma trận kề:")
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    return n, matrix


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


# Nhập thông tin đồ thị từ ma trận kề
n, matrix = input_matrix()

# Chuyển từ ma trận kề sang các dạng khác
edges_from_matrix = convert_to_edge_list_from_matrix(n, matrix)
adj_list_from_matrix = convert_to_adj_list_from_matrix(n, matrix)
edge_matrix_from_matrix = convert_to_edge_matrix_from_matrix(n, matrix)

# Xuất kết quả từ ma trận kề
print("\nDanh sách cạnh kề từ ma trận kề:")
print(f"{n} {len(edges_from_matrix)}")  # Số đỉnh và số cạnh
for edge in edges_from_matrix:
    print(" ".join(map(str, edge)))

print("\nDanh sách đỉnh kề từ ma trận kề:")
for i in range(n):
    print(f"{i + 1}: {adj_list_from_matrix[i]}")

print("\nMa trận cạnh kề từ ma trận kề:")
for row in edge_matrix_from_matrix:
    print(" ".join(map(str, row)))

