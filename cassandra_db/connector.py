from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster

def create_keyspace (session):
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS spark_streams
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)

    print("Keyspace created successfully!")
