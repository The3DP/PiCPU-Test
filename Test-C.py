" python3 -c "
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
runs = 0
while time.time() - start < 10:
    fib(20)
    runs += 1

print(f'Completed {runs} Fibonacci(20) calculations in 10s')
"
