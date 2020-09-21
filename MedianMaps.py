def find_med(inputlist, k):
    if len(inputlist) == 0 or k <= 1:
        return None

    while len(inputlist) > k:
        inputlist = list(map(get_med, (inputlist[x:x + k] for x in (range(0, len(inputlist), k)))))
    return get_med(inputlist)


def get_med(input):
    return sorted(input)[(len(input) - 1) // 2]


if __name__ == '__main__':
    a = [0, 5, 8, 1, 2, 4, 6, 8, 2, 4, 7, 3]
    n = 4
    print(find_med(a, n))
