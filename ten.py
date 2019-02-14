numbers = {}
numbers["one"] = 1
numbers["two"] = 2

cars = {
    'mazda': "red",
    "toyota": "blue",
    "benz": "black"
}

phonebook = {
    "barney": 123456,
    "fred": 554533,
    "carry": 532903444,
    "penny": 53434
}

gps = {
    "Home": '14.75 23.43',
    'Car': '24.33 05.43',
    'Dog': '43.52 45.23'
}

birthdays = {
    "Ted": '2019/02/20',
    'Shantelle': '2081/12/32'
}

reservations = {
    "Ken": '10pm',
    "Ben": "2pm",
    "Urella": "3pm"
}

pets = {
    "dog": "bobby",
    "cat": "Bella",
    "horse": "White Thunder",
}

print(numbers)
print(cars)
print(phonebook)

for object, location in gps.items():
    print(object + " is located at " + location + "")

for name, bd in birthdays.items():
    print("%s birthday is on the date %s" %(name, bd))

print(reservations)
del reservations["Ken"]
print(reservations)

print(pets)
horseName = pets.pop("horse")
print(horseName)
print(pets)

if "dog" in pets:
    print("I have a dog named " + pets["dog"])

if "horse" not in pets:
    print("i no longer have a horse")