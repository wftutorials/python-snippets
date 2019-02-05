myName = "Wynton Franklin"
myNameNoSpace = "WyntonFranklin"
myProfession = 'Software Developer'
makeThisLoud = "Are you happy!"
makeThisSoft = "I AM NOT"
addSign = "+"
listWithCommas = "Hello, Puppies, Blue, Purple"
ageString = "Wynton Age : 53"
addMyAge = "Wynton is {age}"
myPuppiesList = "I have three puppies {0}, {1}, {2}"

print(myName, myProfession)
print(len(myName))
print(len(myNameNoSpace))
print(myName.index("W"))
print(myName.index("n"))
print(myName.index("F"))
print("My last Name " + myName[7:15])
print("My First Name " + myName[0:7])
print("Skip one letters: " + myProfession[0:18:2])
print("Skip two letters: " + myProfession[0:18:3])
print(makeThisLoud.upper())
print(makeThisSoft.lower())
print(myName.startswith("Wynton"))
print(myProfession.endswith("Developer"))
print(myProfession.startswith("Lawyer"))
print(myName.split(" "))
print(myProfession.split()[0])
print(addSign.join(myProfession))
print(addSign.join([myName, myProfession]))
print(listWithCommas.split(","))
print(ageString.partition(':'))
print(addMyAge.format(age="30"))
print(addMyAge.format(age="54"))
print(myPuppiesList.format("Bobby", "Hobby", "Tubby"))