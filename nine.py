class Dog:
    name = "Dog"
    _tail = 1
    _legs = 4
    _ears = 2
    _bark = "roof roof roof"
    _color = "black and white"
    _waggingTail = "wagging tail"
    _age = 0;

    def __init__(self, bark, color):
        self._bark = bark
        self._color = color

    def set_bark(self, bark):
        self._bark = bark

    def get_tail_number(self):
        return self._tail

    def make_noise(self):
        return self._bark

    def wag_tail(self):
        return self._waggingTail

    def get_dog_color(self):
        return self._color

    def set_age(self, age):
        self._age = age

    def calcuate_human_age(self):
        currentAge = self._age
        dogAgeMultipler = 15
        return currentAge * dogAgeMultipler


dog = Dog("roof", "blue and black")
print(dog.make_noise())

prettyDog = Dog("arhooooooo", "brown and grey")
print(prettyDog.make_noise())

prettyDog.set_bark("roof roof roof")
print(prettyDog.make_noise())
prettyDog.set_age(3)
print("dog age " + str(prettyDog.calcuate_human_age()))
