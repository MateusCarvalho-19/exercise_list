#Exercise_01 (Comparador de números)

number_1 = int(input("Please, enter the first number: "))

number_2 = int(input("Please, enter the second number: "))

if number_1 > number_2:
    print(f"Highest number: {number_1}")
elif number_1 == number_2:
    print(f"{number_1} is equal to {number_2}")
else:
    print(f"Highest number: {number_2}") 