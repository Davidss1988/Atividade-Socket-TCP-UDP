import socket

IP = "127.0.0.1"
PORTA = 10410
BUFFER = 1024

# Criação do socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente.connect((IP, PORTA))

print("================================")
print(" CLIENTE DE CONTROLE REMOTO")
print("================================")
print("Conectado ao servidor.")


while True:

    print("\n===== MENU =====")
    print("1 - Ligar sistema")
    print("2 - Desligar sistema")
    print("3 - Consultar status")
    print("4 - Enviar mensagem")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente.send("1".encode("UTF-8"))

    elif opcao == "2":
        cliente.send("2".encode("UTF-8"))

    elif opcao == "3":
        cliente.send("3".encode("UTF-8"))

    elif opcao == "4":
        mensagem = input("Digite a mensagem: ")
        cliente.send(("4|" + mensagem).encode("UTF-8"))

    elif opcao == "5":
        cliente.send("QUIT".encode("UTF-8"))

        resposta = cliente.recv(BUFFER).decode("UTF-8")

        print("\nServidor:", resposta)

        break

    else:
        print("Opção inválida.")
        continue

    resposta = cliente.recv(BUFFER).decode("UTF-8")

    print("\nServidor:", resposta)


cliente.close()

print("\nConexão encerrada.")
