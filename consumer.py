# amqps://lfjntxwl:ajLLnJomCYyxsB1yMZo-dSCdhPl58YSs@hawk.rmq.cloudamqp.com/lfjntxwl

import pika


params = pika.URLParameters('amqps://lfjntxwl:ajLLnJomCYyxsB1yMZo-dSCdhPl58YSs@hawk.rmq.cloudamqp.com/lfjntxwl')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()