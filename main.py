from Kafka.utils import CreateKafkaTopic, SpinUpConsumer, ProduceData
from flask import Flask


app = Flask(__name__)
TOPIC_NAME = ""


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/kafka/<topic_name>')
def kafka(topic_name):
    global TOPIC_NAME
    TOPIC_NAME = topic_name
    CreateKafkaTopic(topic_name)
    SpinUpConsumer(topic_name)

    return "Topic " + topic_name + " created"


@app.route('/producer/<records>')
def producer(records):
    ProduceData(TOPIC_NAME, records)
    return "Producer Starts"
