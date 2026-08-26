import json

tarefas = []
while True:
    print("\n------Menu----")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover Tarefa")
    print("Qualquer outro para sair!")
    resp = input("Escolha 1 opcao ai: ")
    if resp == "1":
        nometarefas = input("Digite o nome da tarerfa: ")
        tarefas.append(nometarefas)

    elif resp == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa adicionada")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(indice + 1, tarefa)

    elif resp == "3":
        tirar = int(input("Qual quer remover?(Digite o numero dela) "))
        tarefas.pop(tirar-1)

    else:
        print("Saindo...")
        break