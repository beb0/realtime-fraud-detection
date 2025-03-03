import random
from uuid import uuid1
from datetime import  datetime

class Generator:

    cities = ['New York', 'Tokyo', 'Barcelona', 'Cairo', 'Berlin', 'Monza']

    def transaction_generator(self):
        return {
            'user_id' : random.randint(1,100),
            'transaction_id': str(uuid1()),
            'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'location': random.choice(self.cities),
            'amount' : round(random.uniform(1,1000000), 2)
        }