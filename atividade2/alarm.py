import pika
from termcolor import colored

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='fire_alert')


def callback(ch, method, properties, body):

    print(colored('Fogo Detectado!', 'red'))
    channel.basic_publish(exchange='', routing_key='fire_prevention_system', body='Ativar sistema de prevenção de incendio')
    print('Sistema de alarme de incendio ativado')


channel.basic_consume(queue='fire_alert', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

