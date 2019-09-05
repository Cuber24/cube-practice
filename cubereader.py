cube = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 16, 27, 28, 29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]


def reorder(lst, a, b, c, d):
    n = lst[d]
    lst[d] = lst[c]
    lst[c] = lst[b]
    lst[b] = lst[a]
    lst[a] = n
    return lst


def move(lst, a):
    if a == 'R':
        reorder(lst, 9, 7, 18, 22)
        reorder(lst, 11, 6, 20, 21)
        reorder(lst, 10, 8, 19, 23)
        reorder(lst, 30, 46, 38, 40)
        reorder(lst, 31, 47, 39, 41)
    elif a == 'L':
        reorder(lst, 0, 14, 15, 5)
        reorder(lst, 1, 12, 16, 3)
        reorder(lst, 2, 13, 17, 4)
        reorder(lst, 26, 42, 34, 44)
        reorder(lst, 27, 43, 35, 45)
    elif a == 'U':
        reorder(lst, 0, 3, 6, 9)
        reorder(lst, 1, 4, 7, 10)
        reorder(lst, 2, 5, 8, 11)
        reorder(lst, 24, 26, 28, 30)
        reorder(lst, 25, 27, 29, 31)
    elif a == 'D':
        reorder(lst, 32, 38, 36, 34)
        reorder(lst, 33, 39, 37, 35)
        reorder(lst, 12, 21, 18, 15)
        reorder(lst, 14, 23, 20, 17)
        reorder(lst, 13, 22, 19, 16)
    elif a == 'F':
        reorder(lst, 0, 10, 21, 13)
        reorder(lst, 1, 11, 22, 14)
        reorder(lst, 2, 9, 23, 12)
        reorder(lst, 24, 41, 32, 43)
        reorder(lst, 25, 40, 33, 42)
    elif a == 'B':
        reorder(lst, 3, 17, 18, 8)
        reorder(lst, 4, 15, 19, 6)
        reorder(lst, 5, 16, 20, 7)
        reorder(lst, 28, 45, 36, 47)
        reorder(lst, 29, 44, 37, 46)
    return lst


def scramble(scr):
    scr = scr.replace(' ', '')
    ns = ''
    for i in range(len(scr)):
        if scr[i] == '2':
            ns = ns + scr[i - 1]
        elif scr[i] == '\'':
            ns = ns + scr[i - 1] + scr[i - 1]
        else:
            ns = ns + scr[i]
    return ns


def read_code(s):
    new_cube = cube.copy()
    for i in scramble(s):
        new_cube = move(new_cube, i)

    return new_cube


if __name__ == '__main__':
    # print(reorder(cube, 3, 17, 31, 46))
    a = input()
    print(read_code(a))
