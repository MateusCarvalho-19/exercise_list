#>>> Exercise_08 <<< (Conversor de Unidade)

while True:
    try: 
        distance = float(input("Please, enter the distance in meters: "))
        break

    except ValueError:
        print("Please, enter numbers only")

unit = {
    1: "centimeters",
    2: "kilometers",
    3: "milimeters"
}

options = "\n".join(
    f"{key} - {value}"
    for key, value in unit.items()
)

while True:
    try: 
        choice = int(input(f"\nChoose a unit:\n \n{options}\n \nOpition: "))

        if choice not in unit:
            print("Invalid unit\n"
                  "Erro: Invalid unit. (Please, enter 1, 2 or 3)")
            continue
        break
    
    except ValueError:
        print("Please, enter only numbers")

if choice == 1:
    cm = distance * 100
    print(f"\nThe distance in {unit[choice]} is: {cm} cm\n")
elif choice == 2:
    km = distance / 1000
    print(f"\nThe distance in {unit[choice]} is: {km} km\n")
elif choice == 3:
    mm = distance * 1000
    print(f"\nThe distance in {unit[choice]} is: {mm} mm\n")