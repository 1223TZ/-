def is_haiku():
    a = input("input string")
    b = a.split("/")
    if len(b) == 3 and len(b[0]) == 5 and len(b[1]) == 7 and len(b[2]) == 5:
        print("True")
    elif b[0] != 5:
        print("False, the error is the first line")
    elif b[1] != 7:
        print("False, the error is the second line")
    elif b[2] != 5:
        print("False, the error is the third line")

is_haiku()

