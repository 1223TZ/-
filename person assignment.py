import random as rd


class Person:
    a = []
    b = []

    def __init__(self, name):
        self.heightint = rd.randint(20, 200)
        self.weight = rd.randint(100, 200)
        self.name = name
        Person.a.append(self.weight)
        Person.b.append(self.heightint)

    def sort_weight(self):
        print(sorted(Person.a))

    def sort_height(self):
        print(sorted(Person.b))

    def weight_mean(self):
        μ1 = sum(Person.a) / len(Person.a)
        return μ1

    def height_mean(self):
        μ2 = sum(Person.b) / len(Person.b)
        return μ2

    def weight_sigma(self):
        for i in Person.a:
            unf = pow(pow((i - (sum(Person.a)/len(Person.a))), 2)/len(Person.a), 1/2)
        print(unf)

    def height_sigma(self):
        for i in Person.b:
            unf2 = pow(pow((i - (sum(Person.b) / len(Person.b))), 2) / len(Person.b), 1 / 2)
        print(unf2)


zhangsan = Person("zhangsan")
lisi = Person("lisi")
wangwu = Person("wangwu")
zhangsan.weight_sigma()
