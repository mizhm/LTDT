"""
input example:
5 9
1 2
1 3
1 4
2 3
2 4
2 5
3 4
3 5
4 5
"""

# Danh sách cạnh kề
def input_graph():
    # Nhập số lượng đỉnh và cạnh
   n, m = map(int, input("Nhập số lượng đỉnh n và số lượng cạnh m: ").split())

   # Khởi tạo danh sách kề
   edges = []
   print(f"Nhập {m} cạnh:")
   for i in range(m):
       # Nhập mỗi cạnh dưới dạng 2 số nguyên u và v
       u, v = map(int, input().split())
       edges.append((u, v))
   return n, m, edges

#convert sang ds đỉnh kề
def convert_to_adj_list(n, edges):
    # Khởi tạo danh sách đỉnh kề
    adj_list = [[] for _ in range(n)]

    # Điền các đỉnh kề vào danh sách
    for u, v in edges:
        adj_list[u - 1].append(v)  # Đỉnh u kề với đỉnh v
        adj_list[v - 1].append(u)  # Đỉnh v kề với đỉnh u (đồ thị vô hướng)

    return adj_list

#convert sang ma trận cạnh kề
def convert_to_edge_matrix(n, edges):
    # Khởi tạo ma trận cạnh kề n x n với tất cả các phần tử bằng 0
    edge_matrix = [[0] * n for _ in range(n)]

    # Điền giá trị vào ma trận cạnh kề
    for u, v in edges:
        edge_matrix[u - 1][v - 1] = 1  # Cạnh nối giữa u và v
        edge_matrix[v - 1][u - 1] = 1  # Cạnh nối giữa v và u (đồ thị vô hướng)

    return edge_matrix


#convert sang ma trận kề
def convert_to_matrix(n, edges):
    # Khởi tạo ma trận kề n x n với tất cả các phần tử bằng 0
    matrix = [[0] * n for _ in range(n)]

    # Điền giá trị vào ma trận theo danh sách cạnh
    for u, v in edges:
        matrix[u - 1][v - 1] = 1  # Chuyển từ chỉ số 1 sang chỉ số 0
        matrix[v - 1][u - 1] = 1  # Đồ thị vô hướng nên cần cập nhật cả hai chiều

    return matrix



# Nhập thông tin đồ thị từ bàn phím
n, m, edges = input_graph()

# Chuyển từ danh sách cạnh sang các dạng khác nhau
matrix = convert_to_matrix(n, edges)
adj_list = convert_to_adj_list(n, edges)
edge_matrix = convert_to_edge_matrix(n, edges)

# Xuất kết quả
print("\nMa trận kề:")
print(n)
for row in matrix:
    print(" ".join(map(str, row)))

print("\nDanh sách đỉnh kề:")
for i in range(n):
    print(f"{i + 1}: {adj_list[i]}")

print("\nMa trận cạnh kề:")
for row in edge_matrix:
    print(" ".join(map(str, row)))