class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('inhale, exhale')

    def get_eyes(self):
        return self.num_eyes


class Fish(Animal):
    def __init__(self):
        super().__init__()

        self.color = 'golden'

    def breathe(self):
        super().breathe()
        print('doing this under water')


dog = Animal()
dog.breathe()

print('-----------------------------------')
fish = Fish()
fish.breathe()
