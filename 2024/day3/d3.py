import re

with open("input.txt") as f:
    s = f.read().strip()

ans = 0
x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", s)
g = True  # Flag for enabled/disabled state

for y in x:
    if y == "do()":
        g = True
    elif y == "don't()":
        g = False
    else:  # Must be a multiplication
        if g:  # Only process if enabled
            # Extract numbers from mul(a,b)
            a, b = map(int, re.findall(r'\d+', y))
            ans += a * b

print(ans)