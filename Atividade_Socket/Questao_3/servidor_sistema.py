import socket

IP = "0.0.0.0"
PORTA = 10410
BUFFER = 1024

# Estado inicial do sistema
sistema_ligado = False

# Criação do socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define IP e porta
servidor.bind((IP, PORTA))

# Aguarda conexão
servidor.listen(1)

print("================================")
print(" SERVIDOR DE CONTROLE REMOTO")
print("================================")
print("Servidor iniciado na porta", PORTA)
print("Aguardando cliente...")

# Aceita conexão
conn, addr = servidor.accept()

print("Cliente conectado:", addr)

while True:

    # Recebe comando do cliente
    dados = conn.recv(BUFFER)

    if not dados:
        break

    comando = dados.decode("UTF-8").strip()

    print("Comando recebido:", comando)

    # Ligar sistema
    if comando == "1":
        sistema_ligado = True
        resposta = "Sistema ligado com sucesso."

    # Desligar sistema
    elif comando == "2":
        sistema_ligado = False
        resposta = "Sistema desligado com sucesso."

    # Consultar status
    elif comando == "3":
        if sistema_ligado:
            resposta = "Status do sistema: LIGADO."
        else:
            resposta = "Status do sistema: DESLIGADO."

    # Enviar mensagem
    elif comando.startswith("4|"):
        mensagem = comando[2:]
        print("Mensagem recebida do cliente:", mensagem)
        resposta = "Mensagem recebida pelo servidor."

    # Encerrar
    elif comando.upper() == "QUIT":
        resposta = "Servidor encerrando a conexão."
        conn.send(resposta.encode("UTF-8"))
        break

    # Comando inválido
    else:
        resposta = "Comando inválido."

    # Envia resposta para o cliente
    conn.send(resposta.encode("UTF-8"))

# Fecha conexão
conn.close()
servidor.close()

print("Servidor encerrado.")