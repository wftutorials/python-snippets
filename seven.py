countDown = [9, 8, 7, 6]

for number in countDown:
    print(number)

print('seperator')

for x in range(6):
    print(x)

print('.........')

for x in range(3, 7):
    print(x)

print('********')

for x in range(6, 10, 2):
    print(x)

print('@@@@@@@@@@@@@@@')

hideSeek=0

while hideSeek < 5:
    print(hideSeek)
    hideSeek += 1

print("!!!!!!!!!!!!")

myAge = 0
while myAge >= 0:
    print(myAge)
    myAge += 1
    if myAge == 10:
        break

print('&&&&&&&&&&&&&&&&&&&&')

for x in range(10):
    if x == 5:
        continue
    else:
        print(x)
