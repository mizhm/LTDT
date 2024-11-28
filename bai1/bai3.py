def main():
    v = 5
    a = {1: [2, 3, 4], 2: [1, 3, 4, 5], 3: [1, 2, 4, 5], 4: [1, 2, 3, 5], 5: [2, 3, 4]}
    e = 0
    b = list()
    b.append([v, e])
    visited = []
    for k, v in a.items():
        visited.append(k)
        for i in range(len(v)):
            if v[i] not in visited:
                b.append([k, v[i]])
                e = e + 1
    b[0][1] = e
    for i in range(len(b)):
        print(b[i])


if __name__ == '__main__':
    main()
