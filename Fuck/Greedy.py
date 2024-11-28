def graph_coloring(graph):
    # Số đỉnh trong đồ thị
    n = len(graph)

    # Khởi tạo mảng màu cho các đỉnh
    color = [-1] * n  # -1 có nghĩa là đỉnh chưa được tô màu

    # Tô màu đỉnh đầu tiên với màu 0
    color[0] = 0

    # Duyệt qua các đỉnh còn lại
    for u in range(1, n):
        # Tạo một mảng để kiểm tra màu nào đã được sử dụng
        used_colors = [False] * n

        # Kiểm tra các đỉnh kề với u và đánh dấu các màu đã được sử dụng
        for v in graph[u]:
            if color[v] != -1:  # Nếu đỉnh v đã được tô màu
                used_colors[color[v]] = True

        # Tìm màu đầu tiên chưa được sử dụng
        for c in range(n):
            if not used_colors[c]:
                color[u] = c
                break

    # Tìm sắc số (số màu tối đa đã sử dụng)
    max_color = max(color) + 1

    # In ra kết quả
    color_groups = {i: [] for i in range(max_color)}
    for u in range(n):
        color_groups[color[u]].append(u + 1)  # +1 vì chúng ta muốn đếm từ 1

    # In kết quả theo yêu cầu
    print(f"Sắc số đồ thị: {max_color}")
    for c in range(max_color):
        print(f"Đỉnh tô màu {c + 1}: {', '.join(map(str, color_groups[c]))}")


# Ví dụ đồ thị
graph = {
    0: [1, 2],  # Đỉnh 1 kề với đỉnh 2 và 3
    1: [0, 3],  # Đỉnh 2 kề với đỉnh 1 và 4
    2: [0, 3],  # Đỉnh 3 kề với đỉnh 1 và 4
    3: [1, 2]  # Đỉnh 4 kề với đỉnh 2 và 3
}

graph_coloring(graph)
