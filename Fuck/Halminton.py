def is_hamiltonian_cycle(graph, path, pos, n):
    # Nếu đã đi qua tất cả các đỉnh, kiểm tra xem có thể quay lại đỉnh đầu tiên không
    if pos == n:
        # Kiểm tra xem đỉnh cuối cùng có kề với đỉnh đầu tiên không
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Duyệt qua tất cả các đỉnh và thử thêm vào đường đi
    for v in range(1, n):
        # Kiểm tra nếu đỉnh v có thể thêm vào đường đi
        if is_safe(graph, v, path, pos):
            path[pos] = v
            if is_hamiltonian_cycle(graph, path, pos + 1, n):
                return True
            # Nếu không tìm thấy, quay lại (backtrack)
            path[pos] = -1
    return False


def is_safe(graph, v, path, pos):
    # Kiểm tra xem đỉnh v có thể thêm vào đường đi hay không
    # Điều kiện 1: Đỉnh v phải kề với đỉnh trước đó
    if graph[path[pos - 1]][v] == 0:
        return False
    # Điều kiện 2: Đỉnh v chưa được thêm vào đường đi
    if v in path:
        return False
    return True


def check_hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n  # Khởi tạo mảng để lưu đường đi
    path[0] = 0  # Bắt đầu từ đỉnh 0

    if is_hamiltonian_cycle(graph, path, 1, n):
        print("Đồ thị có chu trình Hamilton")
    else:
        print("Đồ thị không có chu trình Hamilton")


# Ví dụ đồ thị có chu trình Hamilton
graph_hamiltonian = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]

# Ví dụ đồ thị không có chu trình Hamilton
graph_no_hamiltonian = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

# Kiểm tra chu trình Hamilton
check_hamiltonian_cycle(graph_hamiltonian)  # Kết quả: Đồ thị có chu trình Hamilton
check_hamiltonian_cycle(graph_no_hamiltonian)  # Kết quả: Đồ thị không có chu trình Hamilton
