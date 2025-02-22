import json
import random
import time

from kafka import KafkaProducer
from generator import generator

generator = generator.Generator()

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)


while True:
    transaction = generator.transaction_generator()
    producer.send('transactions_generated',
                 json.dumps(transaction).encode('utf-8'))
    print(f"Sent: {transaction}")
    time.sleep(random.randint(1,10))
