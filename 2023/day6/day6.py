from math import prod
with open("input.txt") as f:
  s = f.read()

def part1():
  time, dist = s.strip().split('\n')
  time = list(map(int, time.split(':')[1].split()))
  dist = list(map(int, dist.split(':')[1].split())) 

  res = []
  for t, d in zip(time, dist):
    count = 0
    for speed in range(t+1):
      dt = speed*(t-speed)
      if dt>d:
        count += 1
    res.append(count)
  print(prod(res))

time, dist = s.strip().split('\n')
time = int("".join(time.split(':')[1].split())) 
dist = int("".join(dist.split(':')[1].split())) 
count = 0
for speed in range(time+1):
  dt = speed*(time-speed)
  if dt>dist:
    count += 1

print(count)