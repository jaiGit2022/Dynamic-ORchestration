import subprocess
from kafka.admin import KafkaAdminClient, NewTopic


def CreateKafkaTopic(topic_name):
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",
        client_id='test'
    )

    topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
    admin_client.create_topics(new_topics=topic_list)

def RemoveKafkaTopic(topic_name):
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",
        client_id='test'
    )

    admin_client.delete_topics([topic_name], timeout_ms=6000)


def SpinUpConsumer(topic_name):
    subprocess.Popen(["python", "Kafka/consumer.py", topic_name])


def ProduceData(topic_name, records):
    print("in producerData")
    subprocess.Popen(["python", "Kafka/producer.py", topic_name, records])


def Rollback(topic_name):
    import Database
    Database.DB.DeleteFromDB(topic_name)
    RemoveKafkaTopic(topic_name)
