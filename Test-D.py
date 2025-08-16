" python3 -c "
import time, math
start = time.time()
ops = 0
while time.time() - start < 10:
    math.sqrt(ops % 1000)
    ops += 1

print(f'Floating-point operations in 10s: {ops}')
"
