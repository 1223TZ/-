def update_frequencies(old_frequencies, new_frequency):
    a = new_frequency.count("A")
    t = new_frequency.count("T")
    g = new_frequency.count("G")
    c = new_frequency.count("C")
    for i in old_frequencies:
        n = list(i)
        if n[0] == "A":
            n[1] += a
            old_frequencies[0] = tuple(n)
        elif n[0] == "T":
            n[1] += t
            old_frequencies[2] = tuple(n)
        elif n[0] == "G":
            n[1] += g
            old_frequencies[3] = tuple(n)
        elif n[0] == "C":
            n[1] += c
            old_frequencies[1] = tuple(n)
    return old_frequencies


f = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
j = "ACCCGTTA"
print(update_frequencies(f, j))
