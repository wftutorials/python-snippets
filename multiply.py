print("Welcome to the multipler")
loop = True

def multipy_function():
    x = input("Enter your first number:\n")
    y = input("Enter your second number:\n")
    sum = int(x) * int(y)
    print("Output = " + str(sum))


while loop:
    multipy_function()
    next = input("Multiple next function? y /n\n")
    if next == "n":
        loop = False
    elif next == "y":
        loop = True
    else:
        loop = False

