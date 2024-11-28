def read_graph_from_input():
    """
    Đọc ma trận kề của đồ thị từ bàn phím.
    Trả về ma trận kề.
    """
    n = int(input("Nhập số lượng đỉnh của đồ thị: "))
    graph = []

    print("Nhập ma trận kề (n x n):")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    return graph, n


def read_graph_from_file(filename):
    """
    Đọc ma trận kề của đồ thị từ tệp tin.
    Trả về ma trận kề.
    """
    with open(filename, 'r') as f:
        n = int(f.readline().strip())  # Đọc số lượng đỉnh
        graph = [list(map(int, f.readline().split())) for _ in range(n)]
    return graph, n


def check_graph_validity(graph, n):
    """
    Kiểm tra tính hợp lệ của đồ thị.
    Đường chéo chính của ma trận kề phải bằng 0 và các cung phải có đỉnh đầu và đỉnh cuối khác nhau.
    """
    for i in range(n):
        if graph[i][i] != 0:
            return False, "Đồ thị không hợp lệ (Đường chéo chính khác 0)"

        for j in range(n):
            if graph[i][j] != 0 and i == j:
                return False, "Đồ thị không hợp lệ (Có cung nối từ đỉnh đến chính nó)"

    return True, "Đồ thị hợp lệ"


def compute_degrees(graph, n):
    """
    Tính bậc của tất cả các đỉnh.
    Trả về danh sách bậc của các đỉnh.
    """
    degrees = [0] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                degrees[i] += 1
    return degrees


def find_min_max_edge(graph, n):
    """
    Tìm cạnh có trọng số nhỏ nhất và lớn nhất của đồ thị.
    Trả về trọng số của cạnh nhỏ nhất và lớn nhất.
    """
    min_weight = float('inf')
    max_weight = float('-inf')

    for i in range(n):
        for j in range(i + 1, n):  # Chỉ xét các cạnh không trùng nhau
            weight = graph[i][j]
            if weight != 0:
                min_weight = min(min_weight, weight)
                max_weight = max(max_weight, weight)

    return min_weight, max_weight


def main():
    # Nhập đồ thị từ bàn phím hoặc tệp tin
    choice = input("Nhập đồ thị từ (1) bàn phím (2) tệp tin: ")

    if choice == '1':
        graph, n = read_graph_from_input()
        # Ghi ma trận kề vào tệp tin
        with open('Test.txt', 'w') as f:
            f.write(f"{n}\n")
            for row in graph:
                f.write(" ".join(map(str, row)) + "\n")
    elif choice == '2':
        filename = input("Nhập tên tệp tin: ")
        graph, n = read_graph_from_file(filename)
    else:
        print("Lựa chọn không hợp lệ!")
        return

    # Kiểm tra tính hợp lệ của đồ thị
    is_valid, message = check_graph_validity(graph, n)
    print(message)

    if not is_valid:
        return

    # Xuất bậc của các đỉnh
    degrees = compute_degrees(graph, n)
    print("Bậc của các đỉnh trong đồ thị:")
    for i in range(n):
        print(f"Đỉnh {i}: Bậc {degrees[i]}")

    # Tìm và xuất cạnh có trọng số nhỏ nhất và lớn nhất
    min_weight, max_weight = find_min_max_edge(graph, n)
    print(f"Cạnh có trọng số nhỏ nhất: {min_weight}")
    print(f"Cạnh có trọng số lớn nhất: {max_weight}")


if __name__ == "__main__":
    main()
