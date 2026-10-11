#<<< Exercise_05 >>> (Reajuste Salarial)

while True:
    try:
        salary = float(input("Please, enter your salary: "))
        break 

    except ValueError:
        print("Please, enter numbers only.")
        continue 

if salary <= 2000:
    percentage = 15
    new_salary = salary + (salary * percentage / 100)
elif salary > 2000.01 and salary <= 5000:
    percentage = 10
    new_salary = salary + (salary * percentage / 100)
else:
    percentage = 5
    new_salary = salary + (salary * percentage / 100)

print(f"\nYou have received a {percentage}% salary increase."
      f"\nYour new salary is: {new_salary:.2f}€\n")