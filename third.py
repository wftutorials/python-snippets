car = 500
people = 100
peopleWhoHateDriving = 10
carNames = "Nissan"
myCarColors = ['red', 'blue', 'green']
yourCarColors = ['black', 'yellow', 'pink']

peopleWithCars = car * people
peopleNotDriving = peopleWithCars - peopleWhoHateDriving
squareThePeople = people ** 2
halfThePeople = people / 2
thirdOfTheCars = car / 3
remainderOfCarsFromThird = car % 3
cubeThePeople = people ** 3
threeNissans = carNames * 3
allCarColors = myCarColors + yourCarColors
repeatMyColors = myCarColors * 3

print("People with Cars " + str(peopleWithCars))
print("Have car don't Drive " + str(peopleNotDriving))
print("Squaring the people " + str(squareThePeople))
print("Cubing the people " + str(cubeThePeople))
print("halfed the people " + str(halfThePeople))
print("Third of The Cars " + str(thirdOfTheCars))
print("Remainder of Cars from Third " + str(remainderOfCarsFromThird))
print(threeNissans)
print("MY Car Colors", myCarColors)
print("Your Car Colors", yourCarColors)
print("All My Cars", allCarColors)
print("My repeated Colors", repeatMyColors)
