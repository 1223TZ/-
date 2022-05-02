def create_entry():
    b = list(a)
    e = []
    for i in range(len(b)):
        if i ==2 or 3:
            e.append(b[i])
    d = dict.update({"HP":b[4],"Attack":b[5],"Defense":b[6],"Sp.Akt":b[7],"Sp.Def":b[8]},"whatever":b[9])
    c = dict(Number=b[0],Name=b[1],Types=tuple(e),BattleStar=d,Generation=b[10],Is_legendary=b[11])
    return c
def main():
    a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel",25, 35, 70, 95, 55, 45, 1, False)

    for key in a_random_pokemon.keys():
      print("{}: {}".format(key, a_random_pokemon[key]))
main()
