class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class HeroSuper(Hero):
    def __init__(self, name, abyliti):
        super().__init__(name, abyliti)

    def __str__(self):
        return f"{self.name} it is super hero"
