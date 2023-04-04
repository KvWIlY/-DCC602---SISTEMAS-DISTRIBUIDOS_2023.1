import socket
import threading
from Crypto.Cipher import AES
import pickle

HOST = 'localhost'
PORT = 8080

# Chave de criptografia (16, 24 ou 32 bytes)
KEY = b'minha_chave_de_criptografia'

# Função para receber as mensagens do servidor
def receive_messages(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        # Descriptografa a mensagem recebida
        cipher = AES.new(KEY, AES.MODE_EAX, nonce=data[:16])
        decrypted_data = cipher.decrypt(data[16:])
        print('\n Mensagem recebida do servidor:', decrypted_data.decode())

# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta ao servidor
    s.connect((HOST, PORT))
    print('Conectado ao servidor')
    # Inicia uma thread para receber as mensagens do servidor
    threading.Thread(target=receive_messages, args=(s,)).start()
    # Loop principal para enviar mensagens para o servidor
    while True:
        message = input('Digite sua mensagem (ou "exit" para sair): ')
        if message == 'exit':
            break
        # Criptografa a mensagem
        cipher = AES.new(KEY, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message.encode())
        nonce = cipher.nonce
        data = pickle.dumps((nonce, ciphertext, tag))
        s.sendall(data)