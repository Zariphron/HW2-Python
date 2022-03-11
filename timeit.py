import time

def calculate_time(called):
    start = time.time()
    called()
    endT = time.time()
    elapsed = endT - start
    return f'Total time {elapsed}'

calculate_time()
