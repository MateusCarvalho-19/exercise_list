#<<< Exercise_03 >>> (Calculadora IMC)

while True:
    try:

        height = float(input("Please, enter your height in meters (e.g., 1.70): "))

        if height <= 0 or height >= 4:
            print("\nInvalid height.\n")
            continue

    except ValueError:
            print("Please, enter only numbers.\n")
            continue
    break

while True:
    try:

        weight = float(input("Please, enter your weight (kg): "))

        imc = weight / (height ** 2)
        imc = round(imc, 2)
        print(f"\nIMC = {imc}")

        if imc < 18.5 :
            print("\nUnderweigth!\n")
        elif imc >= 18.5 or imc <= 24.9:
            print("\nHealthy weight!\n")
        elif imc >= 25:
            print("\nOverweight!\n")
            continue
        break

    except ValueError:
        print("Please, enter only numbers.\n")