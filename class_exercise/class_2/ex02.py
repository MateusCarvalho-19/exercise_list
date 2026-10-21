# Exercício 3: Verificador de Clube (Set + IF/ELIF)
# Objetivo: Usar conjuntos para verificar permissões únicas.
# 1. Crie um Set chamado convidados_vip com 4 nomes de sua escolha.
# 2. Peça para o usuário digitar o seu nome.
# 3. Lógica:
# ○ Se o nome estiver no Set, exiba "Bem-vindo à área VIP!".
# ○ Se o nome for "Dono", exiba "Bem-vindo, chefe!".
# ○ Para qualquer outro nome, exiba "Acesso apenas com convite".

vip_guests = {"Mateus", "Ricardo", "Eduarda", "Guilherme"}

while True:
    guest_name = str(input("Please enter your name: ")).capitalize()

    if guest_name in vip_guests:
        print("\nWelcome to the VIP lounge!\n")
        break
    elif guest_name == "Boss":
        print("\nWelcome, Boss!\n")
        break
    else:
        print("Access by Invitation Only")
        continue