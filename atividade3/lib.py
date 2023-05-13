import random
import os
import signal
import sys
import string
import keyboard
import psutil
import time

# kill no processo do programa atual
def finalizar_programa():
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

def gerar_string(tamanho_bytes):
    """Gera uma string com caracteres aleatórios e o tamanho em bytes especificado."""
    s = ""
    while sys.getsizeof(s) < tamanho_bytes:
        s += random.choice(string.ascii_letters)
    return s

def gera_logs(tamanho_mensagem):
    print("Pressione 'f' para que o servidor comece a gerar logs")
    while True:
        if(keyboard.is_pressed('f')):
            print("\nOs logs comecaram a ser gerados")
            path = os.path.dirname(os.path.realpath(__file__))
            file = open(f"{path}/logs/use_system_{tamanho_mensagem}.txt", "a")
            tempo = 0

            # gera logs em um arquivo por um minuto e finaliza o programa após isso
            while tempo < 60:
                uso_memoria = psutil.virtual_memory().percent
                uso_cpu = psutil.cpu_percent()
                uso_rede = psutil.net_io_counters().packets_recv
                file.write(f"{uso_memoria},{uso_cpu},{uso_rede}\n")
                tempo+=1
                time.sleep(1)
            file.close()
            
            print("Os logs foram gerados com sucesso!")
            finalizar_programa()