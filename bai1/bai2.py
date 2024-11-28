def main():
    v = 5
    a = [[0, 1, 1, 1, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 1, 1, 1, 0]]
    e = 0
    b = list()
    b.append([v, e])
    for i in range(v):
        for j in range(i, v, 1):
            if a[i][j] == 1:
                e = e + 1
                b.append([i + 1, j + 1])
    b[0][1] = e
    for i in range(e):
        print(b[i])


if __name__ == '__main__':
    main()
