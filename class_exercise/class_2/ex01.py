# Crie uma tupla chamada admin_acesso que contém: ("admin", "12345").
# 2. Peça para o usuário digitar o usuario e a senha.
# 3. Lógica:
# ○ Se o usuario for igual ao primeiro item da tupla E a senha for igual ao segundo item, exiba "Acesso
# concedido!".
# ○ Caso contrário, exiba "Login ou senha incorretos".

admin_acces = ("admin", "12345")

while True:
    user = str(input("Please, enter your user: "))
    pass_ = str(input("Please, enter yout password"))

    if user == admin_acces[0] and pass_ == admin_acces[1]:
        print("Acess granted")
        break
    else:
        print("usear and password incorrects")
        continue