import pika
from termcolor import colored

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='temperature')
channel.queue_declare(queue='fire_alert')


def callback(ch, method, properties, body):
    temperature = float(body)
    if temperature > 50:
        channel.basic_publish(exchange='', routing_key='fire_alert', body='FIRE DETECTED!')
        print(colored('Incedio detectado!','red'))
    else:
        print('Temperature:', temperature)

channel.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=True)

print('Aguardando...')
channel.start_consuming()
