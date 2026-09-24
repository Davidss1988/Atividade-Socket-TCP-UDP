import socket
IP = "0.0.0.0"
PORTA = 10410
BUFFER = 1024
# Criação do socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define IP e porta do servidor
servidor.bind((IP, PORTA))
# Aguarda uma conexão
servidor.listen(1)
print("Servidor de chat iniciado.")
print("Aguardando cliente...")
# Aceita a conexão do cliente
conn, addr = servidor.accept()
print("Cliente conectado:", addr)
while True:
    # Recebe mensagem do cliente
    mensagem = conn.recv(BUFFER).decode("UTF-8")
    if not mensagem:
        break
    print("Cliente:", mensagem)
    # Verifica se o cliente encerrou
    if mensagem.upper() == "QUIT":
        print("Cliente encerrou o chat.")
        break
    # Digita resposta para o cliente
    resposta = input("Servidor: ")
    conn.send(resposta.encode("UTF-8"))
    # Verifica se o servidor encerrou
    if resposta.upper() == "QUIT":
        print("Servidor encerrou o chat.")
        break
conn.close()
servidor.close()
print("Servidor encerrado.")