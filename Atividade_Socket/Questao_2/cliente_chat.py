import socket
IP = "127.0.0.1"
PORTA = 10410
BUFFER = 1024
# Criação do socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente.connect((IP, PORTA))

print("Conectado ao servidor.")
print("Digite QUIT para encerrar.")

while True:
    # Digita mensagem
    mensagem = input("Cliente: ")

    # Envia mensagem para o servidor
    cliente.send(mensagem.encode("UTF-8"))

    # Verifica se o cliente encerrou
    if mensagem.upper() == "QUIT":
        print("Chat encerrado.")
        break
    # Recebe resposta do servidor
    resposta = cliente.recv(BUFFER).decode("UTF-8")
    print("Servidor:", resposta)
    # Verifica se o servidor encerrou
    if resposta.upper() == "QUIT":
        print("Chat encerrado pelo servidor.")
        break

# Fecha conexão
cliente.close()