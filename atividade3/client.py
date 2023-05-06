import socket
import threading

def send_message(sock, message):
    sock.sendall(message.encode())

    response = sock.recv(1024).decode()

    print(f"\n -> Resposta recebida: {response}")
    
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost',5000)
    client_socket.connect(server_address)     

    print('Conectado ao servidor...')
    while True:
        mensage = input("\n Digite uma mensagem ou QUIT para sair: ")

        if mensage.lower() == 'quit':
            break

        send_thread = threading.Thread(target=send_message, args=(client_socket, mensage))
        send_thread.start()

    client_socket.close()


if __name__ == "__main__":
    start_client()