#Comentário para o commit
students = {}

for student_count in range(1, 4) :
    while True:
        try:
            print(f"\n --- {student_count}º student informations --- \n")
            student_name = str(input("Please enter your name: "))

            if not student_name.isalpha():
                raise ValueError("name")

            while True:
                try:
                    student_first_grade = input("Please, enter your first grade: ")

                    clean_first = student_first_grade.replace("€", "").replace("$", "").replace(" ", "")

                    if "." in clean_first and "," in clean_first: 
                        clean_first = clean_first.replace(".", "")
                        
                    clean_first = clean_first.replace(",", ".")

                    first_grade = float(clean_first)

                    break

                except ValueError:
                    print("Please, enter numbers only.")
            
            while True:
                try:
                    student_second_grade = input("Please, enter your second grade: ")

                    clean_second = student_second_grade.replace("€", "").replace("$", "").replace(" ", "")

                    if "." in clean_second and "," in clean_second:
                        clean_second = clean_second.replace(".", "")

                    clean_second = clean_second.replace(",", ".")

                    second_grade = float(clean_second)

                    break  

                except ValueError:
                    print("Please, enter numbers only.")

            students[student_name] = (
            first_grade,
            second_grade
        )
            break
            
        except ValueError:
            print("Please, enter alphabetic name.")

print("\nStudents registered:\n")

for student, grades in students.items():
   average = sum(grades) / len(grades)
   if average >= 7:
    print(f"{student}: {average:.2f} - Approved!")
   else:
    print(f"{student}: {average:.2f} - You haven't reached the average.")