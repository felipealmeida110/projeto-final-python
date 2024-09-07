import time
import datetime
dia_hora = datetime.datetime.now()
dia_string = dia_hora.strftime('\033[1;92m%d/%m/%Y\033[m')
hora_string = dia_hora.strftime('\033[1;92m%H:%M:%S\033[m')

def juntar (frase1,frase2):
    return (frase1 + frase2)

frase1 = 'Seja Bem-Vindo'
frase2 = f' a sua Agenda Online hoje é dia: {dia_string} às {hora_string}'

entrada = juntar(frase1,frase2)
print (juntar (frase1,frase2))

tarefas = []

time.sleep(0.5)
print ('Carregando ...')
time.sleep(2)
print ('Escolha sua opção: ')

while True:
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Mostrar Tarefas")
    print("4 - Marcar Tarefa como Concluída")
    print("5 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print('\033[1;31mOpção inválida ! Por favor digite um valor válido\033[m')
        continue

    if opcao == 1:
        tarefa = input("Digite a tarefa: ").upper()
        hora_inicio = datetime.datetime.now().strftime('%H:%M:%S')
        tarefas.append({"tarefa": tarefa, "concluida": False, "hora_inicio": hora_inicio, "hora_conclusao": None})
        time.sleep(1)
        print('Adicionando Tarefa...')
        time.sleep(2)
        print("\033[1;92mTarefa adicionada com sucesso!\033[m")
        time.sleep(2)
        print('Agora escolha sua nova opção')

    elif opcao == 2:
        tarefa = input("Digite a tarefa a ser removida: ").upper()
        for item in tarefas:
            if item["tarefa"] == tarefa:
                tarefas.remove(item)
                time.sleep(0.5)
                print('Carregando...')
                time.sleep(1)
                print("\033[1;92mTarefa removida com sucesso!\033[m")
                time.sleep(2)
                break

            time.sleep(1)

        else:
            print ('Carregando...')
            time.sleep(2)
            print("\033[1;31mTarefa não encontrada!  Verifique a tarefa.\033[m")
            time.sleep(2)


    elif opcao == 3:
        if tarefas:
            time.sleep(1)
            print('Carregando ...')
            time.sleep(2)
            print("Lista de Tarefas:")
            for item in tarefas:
                status = "Concluída" if item["concluida"] else "Pendente"
                hora_inicio = item["hora_inicio"]
                hora_conclusao = item["hora_conclusao"] if item["hora_conclusao"] else "Não concluída ainda"
                print(f"- {item['tarefa']} [{status}] Hora de início: \033[1;31m{hora_inicio}\033[m | Hora de conclusão: \033[1;92m{hora_conclusao}\033[m")
        else:
            time.sleep(1)
            print('Carregando ...')
            time.sleep(2)
            print("\033[1;31mNenhuma tarefa na lista.\033[m")
        time.sleep(2)


    elif opcao == 4:
        time.sleep(1)
        print('Carregando ...')
        time.sleep(2)
        tarefa = input("Digite a tarefa a ser marcada como concluída: ").upper()
        for item in tarefas:
            if item["tarefa"] == tarefa:
                if not item["concluida"]:
                    item["concluida"] = True
                    item["hora_conclusao"] = datetime.datetime.now().strftime('%H:%M:%S')
                    time.sleep(1)
                    print('Carregando ...')
                    time.sleep(2)
                    print("\033[1;92mTarefa marcada como concluída!\033[m")
                else:
                    print("\033[1;92mA tarefa já está concluída.\033[m")
                break
        else:
            time.sleep(1)
            print('Carregando ...')
            time.sleep(2)
            print("\033[1;31mTarefa não encontrada! Verifique a tarefa.\033[m")

        time.sleep(2)

    elif opcao == 5:

        dia_hora = datetime.datetime.now()
        dia_string = dia_hora.strftime('\033[1;92m%d/%m/%Y\033[m')
        hora_string = dia_hora.strftime('\033[1;92m%H:%M:%S\033[m')

        print (f"Fechando a sua Agenda no dia {dia_string} às {hora_string}")
        time.sleep(1)
        print ('Salvando Dados, Por favor Aguarde ...')
        time.sleep(5)
        print ('Dados salvo com sucesso ! ')
        break

    else:
        print('\033[1;31mOpção inválida! Por favor digite uma opção válida!\033[m' )
