import socket
import threading

IP = "0.0.0.0"
PORTA = 10410
BUFFER = 1024

# Estado do sistema
sistema_ligado = False

# Criação do socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permite reutilizar a porta
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Define IP e porta
servidor.bind((IP, PORTA))

# Permite várias conexões
servidor.listen()

print("================================")
print(" SERVIDOR DE CONTROLE REMOTO")
print("================================")
print("Servidor iniciado na porta", PORTA)
print("Aguardando clientes...")


def atender_cliente(conn, addr):
    global sistema_ligado

    print("Cliente conectado:", addr)

    while True:

        dados = conn.recv(BUFFER)

        if not dados:
            break

        comando = dados.decode("UTF-8").strip()

        print("Comando recebido de", addr, ":", comando)

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

            print("Mensagem recebida de", addr, ":", mensagem)

            resposta = "Mensagem recebida pelo servidor."

        # Encerrar conexão
        elif comando.upper() == "QUIT":
            resposta = "Servidor encerrando sua conexão."

            conn.send(resposta.encode("UTF-8"))

            break

        # Comando inválido
        else:
            resposta = "Comando inválido."

        # Envia resposta
        conn.send(resposta.encode("UTF-8"))

    conn.close()

    print("Cliente desconectado:", addr)


# Aceita vários clientes
while True:

    conn, addr = servidor.accept()

    # Cria uma thread para cada cliente
    thread = threading.Thread(
        target=atender_cliente,
        args=(conn, addr)
    )

    thread.start()

    print("Threads ativas:", threading.active_count())
