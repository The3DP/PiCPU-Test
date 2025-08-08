python3 -c "
import threading, time, math, os

def cpu_stress():
    x = 0.0001
    while time.time() < end_time:
        # Do a mix of floating point and integer math
        x = math.sin(x) * math.cos(x) * math.tan(x)
        x += x ** 2
        _ = int(x) % 1234567

duration = 30  # seconds
end_time = time.time() + duration
num_threads = os.cpu_count()

print(f'Starting stress test on {num_threads} threads for {duration} seconds...')

threads = [threading.Thread(target=cpu_stress) for _ in range(num_threads)]
[t.start() for t in threads]
[t.join() for t in threads]

print('Stress test complete.')
"
