# <<< Exercise_00 >>> (Verificador de paridade) 

"""Data request:

"""
try:

    raw_number = input("Please, enter an integer number: ").lower().strip()

#data sanitization - 
    clean_number = raw_number

    if "." in clean_number and "," in clean_number:
        clean_number = clean_number.replace(".", "")

    clean_number = clean_number.replace(",", ".")

    number = float(clean_number)

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    print("Please, enter numbers only.")