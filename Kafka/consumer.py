import sys
import json

from kafka import KafkaConsumer
from Database.DB import InsertIntoDB

topic_name = sys.argv[1]
print("consumer listening on topic : " + topic_name + " .......")
consumer = KafkaConsumer(topic_name, bootstrap_servers=['localhost:9092'])

data = []
for msg in consumer:
    print(msg)
    if msg.value.decode() == "stop":
        break
    print(msg.key)
    obj = {msg.key.decode(): msg.value.decode()}
    data.append(obj)

InsertIntoDB(topic_name, json.dumps(data))
consumer.close()
