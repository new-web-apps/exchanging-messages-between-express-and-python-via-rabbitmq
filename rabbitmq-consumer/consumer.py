import pika

host = 'localhost'
queue = 'my-queue'

def on_message(ch, message, properties, body):
    message = body.decode('UTF-8')
    print(message)

def main():
    connection_params = pika.ConnectionParameters(host=host)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack=True)

    print(f'Subscribing to {queue}, waiting for messages...')
    channel.start_consuming()

# if __name__ - '__main__':
main()

