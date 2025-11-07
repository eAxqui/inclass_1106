def get_age(name, year_of_birth):
    print("Welcome ", name)
    age = 2025 - year_of_birth
    print("Your age is ", age)


get_age("John", 1997)

def cels_to_fah(celsius):

    fahrenheit = (9/5) * celsius +32
    return fahrenheit

def fah_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9

    return celsius

