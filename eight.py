puppyName = "bobby"
firstName = "Wynton"
lastName = "Franklin"


def show_puppy_name():
    print(puppyName)


def add_two_numbers(number1, number2):
    print(number1 + number2)


def add_my_name(primary_name, secondary_name):
    print(primary_name + " " + secondary_name)


def multiple_a_number(number, by):
    return number * by


def divide_a_number(number, by):
    return number / by


show_puppy_name()

add_two_numbers(1, 3)

add_my_name(firstName, lastName)

print(multiple_a_number(8, 2))

print(divide_a_number(100, 2))

print(divide_a_number(multiple_a_number(5, 2), 5))


