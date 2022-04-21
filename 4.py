def get_matryoshka_list(a):
    l = 0
    s = 0
    c = []
    y = 0
    x = 0
    while x < len(a):
        b = a[x]
        if l <= b:
            y += 1
            l = 0
            x += 1
        elif l > b:
            c.append(a[s:y])
            del a[s:y]
            c.append(a[y])
            del a[y]
            y = 0
            s = 0
            x = 0
            l = 0
    c.append(a)
    a = c
    return a


original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
print(get_matryoshka_list(original_list))
