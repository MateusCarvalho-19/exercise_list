#Exercise_01 (Comparador de números)

try:
    raw_first = (input("Please, enter the first number: ")).strip().lower()
    raw_second = (input("Please, enter the second number: ")).strip().lower()

    clean_first = raw_first.replace("€", "").replace("$", "").replace(" ", "")
    clean_second = raw_second.replace("€", "").replace("$", "").replace(" ", "")

    if "." in clean_first and "," in clean_first: 
        clean_first = clean_first.replace(".", "")
    if "." in clean_second and "," in clean_second:
        clean_second = clean_second.replace(".", "")

    clean_first = clean_first.replace(",", ".")
    clean_second = clean_second.replace(",", ".")

    first_number = float(clean_first)
    second_number = float(clean_second)

    if first_number == second_number:
        print(f"{first_number} is equal to {second_number}")
    elif first_number > second_number:
        display_number = int(first_number) if first_number.is_integer() else first_number
        print(f"Highest number: {display_number}")
    else:
        display_number = int(second_number) if second_number.is_integer() else second_number
        print(f"Highest number: {display_number}") 

except ValueError:
    print("Invalid! Please, enter numbers only")