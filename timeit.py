import time

def calculate_time(called):
    def timed():
        start = time.time()
        called()
        endT = time.time()
        elapsed = endT - start
        print(f'Total time {elapsed}')
    return timed
