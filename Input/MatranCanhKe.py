# Hàm nhập đồ thị từ ma trận cạnh kề
def input_edge_matrix():
    # Nhập số lượng đỉnh n
    n = int(input("Nhập số lượng đỉnh n: "))
    edge_matrix = []

    print("Nhập ma trận cạnh kề:")
    for i in range(n):
        edge_matrix.append(list(map(int, input().split())))

    return n, edge_matrix


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
    adj_list = [[] for _ in range(n)]  # Khởi tạo danh sách kề cho mỗi đỉnh

    for u in range(n):
        for v in range(n):
            if edge_matrix[u][v] == 1:
                adj_list[u].append(v + 1)  # Chuyển chỉ số từ 0 -> 1

    return adj_list


# Chuyển từ ma trận cạnh kề sang ma trận kề
def convert_to_matrix_from_edge_matrix(n, edge_matrix):
    matrix = [[0] * n for _ in range(n)]  # Khởi tạo ma trận kề

    for u in range(n):
        for v in range(n):
            if edge_matrix[u][v] == 1:
                matrix[u][v] = 1  # Đặt 1 ở các vị trí có cạnh
                matrix[v][u] = 1  # Đồ thị vô hướng

    return matrix


# Hàm chính để nhập và xuất thông tin đồ thị
def main():
    n = int(input("Nhập số lượng đỉnh n: "))
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
    print(f"{n} {len(edges_from_edge_matrix)}")  # Số đỉnh và số cạnh
    for edge in edges_from_edge_matrix:
        print(" ".join(map(str, edge)))

    print("\nDanh sách đỉnh kề từ ma trận cạnh kề:")
    for i in range(n):
        print(f"{i + 1}: {adj_list_from_edge_matrix[i]}")

    print("\nMa trận kề từ ma trận cạnh kề:")
    for row in matrix_from_edge_matrix:
        print(" ".join(map(str, row)))

# Gọi hàm chính
if __name__ == "__main__":
    main()
