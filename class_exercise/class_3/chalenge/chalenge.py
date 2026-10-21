# O Protocolo "Sentinela de Dados"

# Cenário: Você foi contratado para programar a lógica de um cofre digital de altíssima segurança de uma
# corretora de criptomoedas. O sistema recebe vários dados de uma vez e você precisa decidir se libera a
# trava ou aciona o alarme.

# 1. Preparação dos Dados (Contexto)
# As variáveis iniciais que representam o estado atual do sistema:

#Banco de dados do sistema
#usuarios_bloqueados ={"hakerman", "dr_evil","py.robot"}
#funcionários_ativos = ("ana-gerente", "bruno_tech", "carla_diretora")
#chaves_biometricas = {"setoar_a": "digital_ok", "setor_b", "iris_ok"}

#Tentatival atual (entrada de dados)
#usuario = input("Digite o nome de usuário: ")
#cargo = input("Digite o cargo (gerente, tecnico, estagiario): ")
#possui_cartao = True #simule como se viesse de um sensor
#tentativas_senha = 1

# Python - Desafio 🏆

# Escreva um programa que use apenas um bloco de IF/ELIF/ELSE para validar o acesso. O acesso só será
# concedido se todas as seguintes condições forem verdadeiras:

# 1. Segurança de Lista Negra: O usuario NÃO pode estar no conjunto usuarios_bloqueados.
# 2. Verificação de Hierarquia: O usuario deve estar na tupla funcionarios_ativos.
# 3. Múltiplos Fatores: O usuário deve ter o cartao_id OU saber a "senha mestra" (defina uma senha
# ex: "Python2024").
# 4. Bloqueio de Estagiário: Se o cargo for "estagiario", o acesso é negado automaticamente, mesmo que
# as outras condições sejam verdadeiras.
# 5. Integridade do Sistema: O dicionário chaves_biometricas deve conter a chave "setor_a" com
# o valor "digital_ok".
# 3. Requisitos de Saída (Prints)
# ● Se passar em tudo: " ACESSO LIBERADO. Bem-vindo, [NOME]!"
# ● Se for estagiário: " Acesso negado: Estagiários não possuem nível de acesso ao
# cofre."
# ● Se estiver bloqueado: " ALARME ACIONADO: Usuário na lista de restrição!"
# ● Para qualquer outro erro:

class AuthenticationError (Exception):
    pass

#System database
bloked_users = {"hakerman", "dr_evil","py.robot"}
active_staff = ("ana-gerente", "bruno_tech", "carla_diretora")
biometric_keys = {"setor_a": "digital_ok", "setor_b": "iris_ok"}
position_list = ["manager", "technician", "trainee"]
card_option = {"Yes": True, "No": False}
master_password = ("M@sTerP@ssword")

while True:
    try:
#data entry
        user = str(input("Please, enter your name: ")).lower().strip()
        if user not in active_staff:
            raise AuthenticationError("User not found\n")
        
    except AuthenticationError as e:
            print(e)
            continue

    try:
        if user in bloked_users:
            raise AuthenticationError("\n🚨 ALERT: User on the restricted list! 🚨\n")

    except AuthenticationError as e:
        print(e)
        exit()

    while True:
        try:
            position = str(input("Please, enter your position: ")).lower().strip()
            if position not in position_list:
                raise AuthenticationError("Invalid position")
            elif position == position_list[2]:
                raise AuthenticationError("You do not have permission for this access. Access denied.")
            
        except AuthenticationError as e:
            print(e)
            exit()

        while True:
            try:
                card = str(input(f"Do you have a card ?\n"  f"\n{', '.join(card_option.keys())}\n  \nOption: ")).capitalize()
                card = card_option[card]

                if card:
                    for biometric in biometric_keys.values():
                        for i in range(3):
                            print(".\n")
                        print(biometric, "\n")

                elif not card:
                    password_attempts = 0
                    max_attempts = 3
                    while password_attempts < max_attempts:
                        password = str(input("Please, enter the master password: "))
                        if password == master_password:
                            break
                        else:
                            password_attempts += 1  
                            print("\nIncorret password!\n")  
                            if password_attempts >= max_attempts:
                                raise AuthenticationError("Access denied. Please try later.\n")
                            continue

            except AuthenticationError as e:
                print(e)
                exit()
        
            print(f"Access granted!\nWelcome {user}\n")
            break
        break
    break