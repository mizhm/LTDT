def main():
    v = 5
    e = 9
    a = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    flatten_list = list(set(x for row in a for x in row))
    b = {key: [] for key in flatten_list}
    for i in range(len(a)):
        k, v = a[i]
        b[k].append(v)
        b[v].append(k)
    print(v)
    for k, v in b.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
    print((65 ** 11) % 1763)
