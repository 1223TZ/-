def haiku_string_parser(a):
    b = a.split("/")
    for i in b:
        for e in i:
            if e == ",":
                continue
            else:
                print(e, end = "")
        print("")
    return a


haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
haiku_string_parser(haiku_string)
