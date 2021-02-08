## **Dynamic Orchestration SAGA**
### _This repo contains the code of my prohibition project_

`/Kafa` contains the file related to kafka i.e. Consumer, Producer
`/Kafka/Database` contains the database related files.
`/main.py` is client app using flask

### **Prerequisite**
_PostgreSQL installed_
#### _Kafka zookeper running_
`bin/zookeeper-server-start.sh config/zookeeper.properties
`
#### _Kafka broker running_
`bin/kafka-server-start.sh config/server.properties
`
### **Steps to run code**
### _Install requirements by running_
`pip install -r requirments.txt
`

### _Export **FLASK_APP** variable_
`export FLASK_APP=hello.py
`

### _Run Code_
`flask run
`