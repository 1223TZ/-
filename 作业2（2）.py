def create_entry(a, b, c, d, e, f, g, h, i, j, k, l):
    if d == "":
        n = dict({"HP": d, "Attack": e, "Defense": f, "Sp.Akt": g, "Sp.Def": h, "whatever": i})
        z = dict(Number=a, Name=b, Types=c, BattleStar=n, Generation=j, Is_legendary=k)
    else:
        x = (c,d)
        n = dict({"HP": e, "Attack": f, "Defense": g, "Sp.Akt": h, "Sp.Def": i, "whatever": j})
        z = dict(Number=a, Name=b, Types=x, BattleStar=n, Generation=k, Is_legendary=l)
    return z


def main():
    a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel", 25, 35, 70, 95, 55, 45, 1, False)

    for key in a_random_pokemon.keys():
        print("{}: {}".format(key, a_random_pokemon[key]))


main()
