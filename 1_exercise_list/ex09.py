#>>> Exercise_09 <<< (Simulador de Caixa Eletrônico)

while True:
    try:
        amount = int(input("Please, enter the amount you would like to withdraw: €"))

        if amount <= 0:
                raise ValueError
        break
    
    except ValueError:
        print("Invalid amount! Please enter whole numbers only.")

notes = [50, 20, 10]
banknotes = {}

for note in notes:
    quantity = amount // note
    banknotes[note] = quantity
    remaining = amount % note
    amount = remaining

if amount == 0:
    print("Withdrawal completed successfully.")

    for notes, quantity in banknotes.items():
        if quantity > 0:
            print(f"${notes} banknotes: {quantity}")

else:
    print("The withdrawal cannot be completed using the available banknotes.")