import logging
from cassandra.cluster import Cluster

def create_keyspace (session):
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS spark_streams
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)

    print("Keyspace created successfully!")

def create_txn_table(session):
    session.execute("""
    CREATE TABLE IF NOT EXISTS spark_streams.transactions (
        user_id INT,
        transaction_id UUID PRIMARY KEY,
        date_time TIMESTAMP,
        location TEXT,
        amount int
        );
    """)

    print("Table created successfully!")

def insert_data(session, **kwargs):
    print("inserting data...")

    user_id = kwargs.get('user_id')
    transaction_id = kwargs.get('transaction_id')
    date_time = kwargs.get('date_time')
    location = kwargs.get('location')
    amount = kwargs.get('amount')

    try:
        session.execute("""
            INSERT INTO spark_streams.transactions(user_id, transaction_id, date_time, location, address, 
                amount)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (user_id, transaction_id, date_time, location, amount))
        logging.info(f"Data inserted for {user_id}")

    except Exception as e:
        logging.error(f'could not insert data due to {e}')

def create_cassandra_connection():
    try:
        # connecting to the cassandra_db cluster
        cluster = Cluster(['localhost'])

        cas_session = cluster.connect()

        return cas_session
    except Exception as e:
        logging.error(f"Could not create cassandra connection due to {e}")
        return None

if __name__ == "__main__":
    session = create_cassandra_connection()
    create_keyspace(session)
    create_txn_table(session)