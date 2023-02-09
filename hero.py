class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def get_health_points(self):
        return self.health_points * 2

    def __len__(self):
        return len(self.catchphrase)

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'


superhero = SuperHero('Roma', 'Romachmo', 'fly', 100, 'yachmo')
print(superhero)
print(superhero.get_name())
print(superhero.get_health_points())
print(superhero.__len__())

class StoneHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def get_health_points(self):
        self.fly = True
        self.health_points **= 2
        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')


class CosmoHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def get_health_points(self):
        self.fly = True
        self.health_points **= 2
        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')


stoneHero = StoneHero('tor', 'z', 'Chris Hemsworth', 500, 'loki lox!!!', 100)
stoneHero.get_health_points()
stoneHero.method_fly()



cosmoHero = CosmoHero('flash', 'bari', 'speed', 700, 'speeeeed', 150)
cosmoHero.get_health_points()
cosmoHero.method_fly()


class Villain(CosmoHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        CosmoHero.__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self):
        return self.damage ** 2


villain = Villain('batman', 'bat', 'beast', 1000, 'All heroes must to die!!!')

print(villain.crit(stoneHero))
