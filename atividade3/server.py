import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # Recebe a mensagem do cliente
            data = client_socket.recv(1024)

            if not data:
                print(f"Cliente {client_socket.getpeername()} se desconectou.")
                break

             # Inverte a mensagem recebida
            message = data.decode()[::-1].encode()

            # Envia a mensagem invertida de volta para o cliente
            client_socket.send(message)
        except:
            print(f"Erro na conexão com o cliente {client_socket.getpeername()}")
            break
    client_socket.close()

def start_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o IP e a porta em que o servidor deve ouvir
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)

    # Define o número máximo de conexões simultâneas
    server_socket.listen(5)

    print(f'Servidor iniciado em {server_address}')

    while True:
        # Aceita uma conexão e cria uma nova thread para atendê-la
        client_socket, client_address = server_socket.accept()
        print(f'Nova conexão de {client_address}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_server()
