" python3 -c "
import threading, time

def stress():
    x = 0
    while time.time() < end_time:
        x += 1

num_threads = 4
duration = 10
end_time = time.time() + duration

threads = [threading.Thread(target=stress) for _ in range(num_threads)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f'Multithreaded stress test completed for {duration} seconds')
"
