# Exercício 1: Gerenciador de Lista de Tarefas (List + IF)
# Objetivo: Praticar busca e existência em listas.
# 1. Crie uma lista chamada tarefas com: "Estudar Python", "Limpar quarto", "Fazer exercícios".
# 2. Peça para o usuário digitar uma nova tarefa.
# 3. Lógica: Se a tarefa já estiver na lista (use o operador in), exiba "Essa tarefa já existe!". Caso contrário, adicione-a à
# lista com .append() e exiba a lista atualizada.

tasks = ["study Python", "clean room", "workout"]

while True:
    new_task = str(input("Please, enter the task: ")).lower()

    if new_task in tasks:
        print("This task is already in the task list\n")
        continue
    else:
        tasks.append(new_task)
        print("\n".join(tasks))
        break