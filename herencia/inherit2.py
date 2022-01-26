class Child:
    def __init__(self):
        self.hair_color = 'brown'
        self.is_living_in_house = True
        self.earny_money = True

    def walk(self):
        print("I'm walking")

    def playVideogame(self):
        print('Likes playing videogames')

class Father(Child):
    def __init__(self):
        super().__init__()
        self.age = 45
    def walk_to_work(self):
        super().walk()
        print('to the job')

    def playVideogam_at_Night(self):
        super().playVideogame() 
        print('at night')
        


child = Child()
father = Father()

child.walk()
father.walk_to_work()

