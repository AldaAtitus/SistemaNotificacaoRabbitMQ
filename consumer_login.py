import pika
import json

url = "amqps://wezzidbt:pEABp7TrvywHGow8T0u6iQiF1BikJpsB@jackal.rmq.cloudamqp.com/wezzidbt"

params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='login_queue', durable=True)

def callback(ch, method, properties, body):
    msg = json.loads(body)
    print(f"[LOGIN] {msg['user']} acabou de fazer login!")

channel.basic_consume(queue='login_queue', on_message_callback=callback, auto_ack=True)

print(" [*] Esperando mensagens de login...")
channel.start_consuming()
