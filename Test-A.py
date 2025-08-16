" python3 -c "
import time
start = time.time()
count = 0
while time.time() - start < 10:
    count += 1 * 2 / 3 - 4 + 5
print(f'Arithmetic operations in 10s: {count}')
"
