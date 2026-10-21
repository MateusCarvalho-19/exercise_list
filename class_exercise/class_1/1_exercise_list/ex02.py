#<<< Exercise_02 (Login de acesso) >>>

class AuthenticationError(Exception):
    pass

while True:
    try:

        user = input("Please enter yor user id: ")

        password = str(input("Please, enter your password: "))

        if user == "admin" and password == "1234":
            print("\nAcess granted: Welcome, administrator!\n")
            break
        elif user == "admin" and password != "1234":
            raise AuthenticationError("\nIncorret password!\n")
        else:
            raise AuthenticationError("\nUser not recognized. Access denied.\n")
          

    except AuthenticationError as e:
        print(e)