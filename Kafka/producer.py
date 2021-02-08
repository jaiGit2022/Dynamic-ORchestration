import sys
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic_name = sys.argv[1]
records = sys.argv[2]

print("producer sending data on topic : " + topic_name + " .......")


for i in range(int(records)):
    key = "key" + str(i + 1)
    value = "value" + str(i + 1)
    future = producer.send(topic_name, key=str.encode(key), value=str.encode(value))

future = producer.send(topic_name, b'stop')

print(future.get())
producer.close()
