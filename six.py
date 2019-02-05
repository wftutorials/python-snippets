number = 4
number1 = 5
number2 = 6
isDogReal = True
isDogFake = True
carRunning = False
doorOpen = True
speed = 30
yourPassword = "stupidLength"
aWallet = ["dollors", "cents", "cards"]
walletTag = "cardss"
treasureChest = "gold"
treasureItem = "gold"
counter = 10
numbersObj = [1, 2, 3]
numbersOtherObj = [1, 2, 3]


print(number == 4)
print(number1 != 4)
print(number == 7)

if isDogReal:
    print("Yes dog is reald")

if isDogFake != False:
    print("Dog is fake")

if carRunning:
    print("Car is running")
else:
    print("Car not running")

if carRunning or doorOpen:
    print("Don't go outside")
else:
    print("You can leave the car")

if yourPassword == "stupidLength":
    print("This password works")
else:
    print("this password doesnt work")

if walletTag in aWallet:
    print("You have " + walletTag)

if treasureItem in treasureChest:
    print("You have gold")
elif treasureItem in treasureChest:
    print("you have silver")

if counter == 4:
    print("counter = 4")
elif counter == 5:
    print("counter = 5")
else:
    print("Counter is whatever it is")

print(not isDogFake)

print(numbersObj == numbersOtherObj)
print(numbersObj is numbersOtherObj)