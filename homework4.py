class A:

    def __init__(self, name):
        self.name = name


class B:

    def __init__(self, age):
        self.age = age


class C:

    def math(self):
        print(f'{self.age} раз красавчик')

class D:
    def gogo(self):
        print(f'{self.name} красавчик')

class E(A, B, C, D):
    def __init__(self, name, age):
        A.__init__(self ,name)
        B.__init__(self ,age)


p = E(name='alim', age=17)
p.math()
p.gogo()


