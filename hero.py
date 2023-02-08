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


class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name

        self.nickname = nickname

        self.superpower = superpower

        self.health_points = health_points

        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)

    def health_2(self):
        self.health_points *= 2

        print(f"Updated health points: {self.health_points}")

    def __str__(self):
        return f"Nickname -> {self.nickname} \n" \
               f"SuperPower -> {self.superpower} \n" \
               f"Health -> {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


barbie = SuperHero("Aijamal", "aijamal.08", "Screaming", 200, "Baidoolot Yilak")

barbie.print_name()

barbie.health_2()

print(barbie)

print(len(barbie))

print()


class StoneHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

        self.damage = damage

        self.fly = fly

    def health_2(self):
        self.fly = True

        self.health_points **= 2

        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')


class CosmoHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

        self.damage = damage

        self.fly = fly

    def health_2(self):
        self.fly = True

        self.health_points **= 2

        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')


stoneHero = StoneHero('tor', 'z', 'Chris Hemsworth', 500, 'loki lox!!!', 100)

print(stoneHero)

stoneHero.health_2()

stoneHero.method_fly()

print()

cosmoHero = CosmoHero('flash', 'bari', 'speed', 700, 'speeeeed', 150)

print(cosmoHero)

cosmoHero.health_2()

cosmoHero.method_fly()

print()


class Villain(CosmoHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self, hero):
        return hero.damage ** 2


villain = Villain('batman', 'bat', 'beast', 1000, 'All heroes must to die!!!')

print(villain.crit(stoneHero))
