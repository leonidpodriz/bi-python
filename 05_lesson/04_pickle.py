import pickle
from datetime import datetime

data = {
    'key': datetime.now()
}

with open('dump.bin', 'wb') as file:
    pickle.dump(data, file)
