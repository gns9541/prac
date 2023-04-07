class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def bark(self, barking):
        self.barking = barking
        return (f"{self.name}가 {barking}짖는다")
    
    def birth_dog(self, num):
        self.birth_of_dogs = num
        self.num_of_dogs += num


    def get_status(self, birth_of_dogs, death):
        self.num_of_dogs = birth_of_dogs - death
        return (f"태어난 강아지는 {birth_of_dogs} 마리 입니다\n현재 개는 {self.num_of_dogs} 마리 입니다")     

a_dog = Doggy("토리", "포메")
a_dog.birth_dog(1)
print(a_dog.name, a_dog.species)
print(a_dog.bark("멍멍"))
print(a_dog.get_status(1,0))




