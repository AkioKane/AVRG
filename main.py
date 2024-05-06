import random
import time

class AVRG():
    
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
    
    def generate(self):
        voltage = random.uniform(0, 5)
        time.sleep(0.1) # Задержка
        random_number = (voltage * 1000) / 100
        
        return random_number

if __name__ == '__main__':
    rg = AVRG()
    
    for i in range(10):
        print(rg.generate())
