#<<< Exercise_04 >>> (Aprovado ou Reprovado)

while True:
    try:

        first_grade = float(input("Please, enter your first grade: "))
        break

    except ValueError:
        print("Please, enter numbers only")
        continue

while True:
    try:
        second_grade = float(input("Please, enter your second grade: "))
        break
        
    except ValueError:
        print("Please, enter numbers only")
        continue

while True:
    try:
        third_grade = float(input("Please, enter your third grade: "))
        break
        
    except ValueError:
        print("Please, enter numbers only")
        continue

print(f"\nFirst Grade: {first_grade}"
      f"\nSecond Grade: {second_grade}"
      f"\nThird Grade: {third_grade}")

avarage = (first_grade + second_grade + third_grade) / 3

print(f"\nYour avarage is: {avarage:.2f}")

if avarage >= 7:
    print("\nPassed!\n")
elif avarage >= 5 or avarage <= 6.9:
    print("\nRemedial.\n")
else:
    print("\nFailed.\n")