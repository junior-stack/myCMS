---
date:
    created: 2025-10-10
draft: true
tags:
  - Programming
---
My notes about common backend framework, libraries and microservices
<!-- more -->
Communication:
- gRPC
- HTTP/HTTPS rest
- graphQL
- websocket
- server-sent events

# 1. Kafka
Go: https://www.youtube.com/watch?v=j6bqJKxb2w0
python & Flink: https://www.youtube.com/watch?v=FoypLT2W91c
java: https://www.youtube.com/watch?v=bxmvfgY0ZI0
end to end: https://www.youtube.com/watch?v=GqAcTrqKcrY
message app: https://upstash.com/blog/next-chatapp-with-kafka

## 1.2 Minimal boot up
minimal docker compose.yaml to launch kafka:
- kafka(7.5.0)
```yaml
version: "3.9"
services:
	zookeeper:
		image: confluentinc/cp-zookeeper
		environment:
			ZOOKEEPER_TICK_TIME: 2000
			ZOOKEEPER_CLIENT_PORT: 32181
	kafka:
		image: confluentinc/cp-kafka:7.5.0
		depends_on:
			- zookeeper
		environment:
			KAFKA_BROKER_ID: 1 
			KAFKA_ADVERTISED_HOST_NAME: 0.0.0.0
			KAFKA_ZOOKEEPER_CONNECT: zookeeper:32181
			KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,HOST://0.0.0.0:29092
			KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,HOST://localhost:29092
			KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,HOST:PLAINTEXT
			KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
			KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
		ports:
	      - "9092:9092" 
	      - "29092:29092"
volumes:
	settings:
	data:
```
- latest kafka(kraft mode):
```yaml
version: '3.8'
services:
  kafka:
    image: confluentinc/cp-kafka:latest
    hostname: kafka
    container_name: kafka
    ports:
      - "9092:9092"
      - "9093:9093"
    environment:
      KAFKA_KRAFT_MODE: "true"
      KAFKA_PROCESS_ROLES: controller,broker
      KAFKA_NODE_ID: 1
      KAFKA_CONTROLLER_QUORUM_VOTERS: "1@localhost:9093"
      KAFKA_LISTENERS: "HOST://0.0.0.0:9092,DOCKER://0.0.0.0:9093"
      KAFKA_ADVERTISED_LISTENERS: "HOST://localhost:9092,DOCKER://kafka:9093"
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: "HOST:PLAINTEXT,DOCKER:PLAINTEXT"
```
Notes about kafka environment variables:
- KAFKA_LISTENERS: 
	- defines all listeners needed for kafka containers. each listener may serve different purposes at the same, either for consumer/producer or inter-broker communication
	- contain at least two listeners
	- each listener format: `<LISTENER_NAME>://0.0.0.0:<LISTENER_PORT>`
	- ports of below config must include subset ports of this KAFKA_LISTENERS;
- KAFKA_ADVERTISED_LISTENERS: 
	- specify which listeners from KAFKA_LISTENERS listen from producer/consumer
	- each listener format: `<LISTENER_NAME>://<HOSTNAME>:<LISTENER_PORT>`
	- `<LISTENER_PORT>` must be subset ports from above
	- we distribute listener_ports either to listen from internal docker network or external IPs/host from public net by specifying the associated `<HOSTNAME>` to be either this broker container name or `localhost`
- KAFKA_INTER_BROKER_LISTENER_NAME: specify listeners from KAFKA_LISTENERS with this name listen for inter-broker communications
- KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: map `<LISTENER_NAME>` to real protocols

| Var             | Role                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KAFKA_LISTENERS | - defines all listeners needed for kafka containers. each listener may serve different purposes at the same, either for consumer/producer or inter-broker communication<br>- contain at least two listeners<br>- each listener format: `<LISTENER_NAME>://0.0.0.0:<LISTENER_PORT>`<br>- ports of below config must include subset ports of this KAFKA_LISTENERS;<br> |
|                 |                                                                                                                                                                                                                                                                                                                                                                      |


##  1.3 Producer code
```python
# pip install python-kafka
from kafka import KafkaProducer

# KAFKA_ADVERTISED_LISTENERS contains <LISTENER_NAME>://localhost:29092
kafka_nodes = "localhost:29092"
myTopic = "weather"

def gen_data():
    prod = KafkaProducer(bootstrap_servers=kafka_nodes, value_serializer=lambda x:dumps(x).encode('utf-8'))
    my_data = {'city': "Shanghai", 'temperature': random.uniform(10.0, 110.0)}
    prod.send(topic=myTopic, value=my_data)
    prod.flush()
```

## 1.4 Consumer code
```python
# pip install python-kafka
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'weather',
    bootstrap_servers='localhost:29092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(message.value)
```

# 2. Flink

# 3. OAuth

# 5. Reddis
## 5.1 Cache

## 5.2 Distributed lock

## 5.3 Share user's session
When you config load balancer, the load balancer may distribute user's requests into different server IPs. For ex, load balancer first direct user to Server A, then the next request to server B. server B does not have session infor from server A. That's when we need to share user's session in redis.

# 4. Payment
