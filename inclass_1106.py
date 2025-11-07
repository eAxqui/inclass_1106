import myutils

def get_age(name, year_of_birth):
    print("Welcome ", name)
    age = 2025 - year_of_birth
    print("Your age is ", age)


get_age("John", 1997)

# Celsius to Fahrenheit conveter function
def cels_to_fah(celsius):
    fahrenheit = (9/5) * celsius +32

    return fahrenheit

# Fahrenheit to Celsius converter function
def fah_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9

    return celsius

# Output test for celsius to fahrenheit
answer_one = cels_to_fah(30)
print(answer_one)

# Output test for fahrenheit to celsius
answer_two = fah_to_cels(86)
print(answer_two)


"""
Documentation comment init
"""

print(print.__doc__)