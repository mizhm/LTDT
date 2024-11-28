class Dsu:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # Đại diện cho mỗi tập
        self.rank = [0] * (n + 1)  # Độ sâu của cây

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges):
    dsu = Dsu(n)  # Khởi tạo DSU
    edges.sort(key=lambda x: x[2])  # Sắp xếp các cạnh theo trọng số tăng dần
    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if dsu.union(u, v):  # Nếu hợp nhất được hai tập hợp
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges

# Ví dụ input
n = 4
edges = [
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 3),
    (4, 1, 4)
]

# Tìm cây khung nhỏ nhất với Kruskal
mst_weight, mst_edges = kruskal(n, edges)
print("Tổng trọng số:", mst_weight)
print("Các cạnh trong cây khung nhỏ nhất:", mst_edges)
