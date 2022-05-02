def get_nucleotide_frequencies(a):
    count1 = a.count("A" or "a")
    count2 = a.count("G" or "g")
    count3 = a.count("C" or "c")
    b = list(a)
    for e in range(len(b) - 1, -1, -1):
        if b[e] == "A":
            b.pop(e)
        elif b[e] == "G":
            b.pop(e)
        elif b[e] == "C":
            b.pop(e)
    s = set(b)
    d = {}
    for i in s:
        d.update({i: b.count(i)})
    print(dict({"A": count1, "C": count3, "G": count2, "Junk": d}))


get_nucleotide_frequencies("ACTGTCACGRFRTNHYCTCGACCSGTGTCACGT")
