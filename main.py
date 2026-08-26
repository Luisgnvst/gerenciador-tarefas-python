tarefas = []
while True:
    print("\n------Menu----")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")
    resp = input("Escolha 1 opcao ai: ")
    if resp == "1":
        nometarefas = input("Digite o nome da tarerfa: ")
        tarefas.append(nometarefas)

    elif resp == "2":
        print(tarefas)

    else:
        print("Saindo...")
        break