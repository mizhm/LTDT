def main():
    v = 5
    e = 9
    a = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    b = [[0] * v for i in range(v)]
    for i in range(e):
        [x, y] = a[i]
        b[x - 1][y - 1] = 1
        b[y - 1][x - 1] = 1
    for i in range(len(b)):
        print(b[i])


if __name__ == '__main__':
    main()
