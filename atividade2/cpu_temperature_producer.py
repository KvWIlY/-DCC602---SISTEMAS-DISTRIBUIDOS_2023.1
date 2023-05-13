import pika
import psutil
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='temperature')

def publish_temp_cpu():
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    channel.basic_publish(exchange='', routing_key='temperature', body=str(temperature))

while True:
    publish_temp_cpu()
    time.sleep(5)