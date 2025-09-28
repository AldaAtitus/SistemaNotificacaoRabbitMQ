import pika
import json

url = "amqps://wezzidbt:pEABp7TrvywHGow8T0u6iQiF1BikJpsB@jackal.rmq.cloudamqp.com/wezzidbt"
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='log_queue', durable=True)

def callback(ch, method, properties, body):
    msg = json.loads(body)
    print(f"[LOG] {msg['user']} executou o evento: {msg['event']}")


channel.basic_consume(queue='log_queue', on_message_callback=callback, auto_ack=True)

print(" [*] Esperando mensagens de log...")
channel.start_consuming()
