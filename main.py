import json
def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

tarefas = carregar_tarefas()
while True:
    print("\n------Menu----")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover Tarefa")
    print("Qualquer outro para sair!")
    resp = input("Escolha 1 opcao ai: ")
    if resp == "1":
        nometarefas = input("Digite o nome da tarefa: ")
        tarefas.append(nometarefas)
        salvar_tarefas()

    elif resp == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa adicionada")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(indice + 1, tarefa)

    elif resp == "3":
        tirar = int(input("Qual quer remover?(Digite o numero dela) "))
        tarefas.pop(tirar-1)
        salvar_tarefas()

    else:
        print("Saindo...")
        break