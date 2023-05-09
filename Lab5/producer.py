from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while True:
    message = str(int(time.time()))
    producer.send('common', message.encode())