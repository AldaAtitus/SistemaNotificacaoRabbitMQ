import pika
import json
from datetime import datetime


url = "amqps://wezzidbt:pEABp7TrvywHGow8T0u6iQiF1BikJpsB@jackal.rmq.cloudamqp.com/wezzidbt"
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='user_events', exchange_type='direct', durable=True)

def send_event(user, event):
    message = {
        "user": user,
        "event": event,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    channel.basic_publish(
    exchange='user_events',
    routing_key='user.login', 
    body=json.dumps(message)
)


    print(f"[PRODUTOR] Enviada mensagem: {message}")

# Exemplos
send_event("João", "user.login")
send_event("Maria", "user.upload")
send_event("Pedro", "user.logout")

connection.close()
