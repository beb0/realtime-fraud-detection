def kafka_txn_producer():
    import json
    import logging
    import random
    import time
    from kafka import KafkaProducer
    from kafka_producer.generator import generator

    generator = generator.Generator()

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    while True:
        try:
            transaction = generator.transaction_generator()
            producer.send('transactions_generated',
                          json.dumps(transaction).encode('utf-8'))
            print(f"Sent: {transaction}")
            time.sleep(random.randint(1, 10))
        except Exception as e:
            logging.error(f"Error: {e}")
            continue
