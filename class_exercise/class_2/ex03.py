# Exercício 4: Classificador de Notas (Dict + ELIF)
# Objetivo: Mapear dados e aplicar lógica de classificação sobre os valores.
# 1. Crie um dicionário chamado boletim com 3 matérias e suas respectivas notas (ex: {"Matematica": 8.5, "Portugues":
# 6.0, "Historia": 4.5}).
# 2. Peça para o usuário digitar o nome de uma matéria.
# 3. Lógica:
# ○ Se a matéria existir no dicionário:
# ■ Se a nota for >= 7: exiba "Aprovado em [Matéria]".
# ■ Se a nota for entre 5 e 6.9: exiba "Recuperação em [Matéria]".
# ■ Se for menor que 5: exiba "Reprovado em [Matéria]".
# ○ Se a matéria não existir no dicionário, exiba "Matéria não encontrada".

report_card = {
    "math": 8.5,
    "english": 5.0,
    "physics": 4.3
}

while True:
    subject = str(input("Please, enter the subject: ")).lower()

    if subject in report_card:
        if report_card[subject] >= 7:
            print(f"You are approved in {subject}")
        elif report_card[subject] >= 5 and report_card[subject] <= 6.9:
            print(f"You are remedial in {subject}")
        elif report_card[subject] < 5:
            print(f"You have failed in {subject}")
        break

    else:
        print("Subject not found")
        continue