with open("input.txt") as f:
  s =  f.read().strip()

lines = s.split("\n\n")
inputs = [int(x) for x in lines[0].split(':')[1].split()] 
# print(seeds)
seed, *others = lines
# seed = seed.split(':')[1].split()

def part1(inputs, others):
  for o in others:
    ranges = []
    for lines in o.splitlines()[1:]:
      ranges.append(list(map(int, lines.split())))

    new = [] 
    for x in inputs:
      for d, s, r in ranges:
        if x in range(s, s+r):
          new.append(x-s+d)
          break
      else:
        new.append(x)
    inputs = new
  print(min(inputs))
# part1(inputs, others)

def part2(inputs, blocks):
  seeds = []

  for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i]+inputs[i+1]))

  for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
      ranges.append(list(map(int, line.split())))

    new = []
    while len(seeds)>0:
      s, e = seeds.pop()
      for a, b, c in ranges:
        os = max(s, b)
        oe = min(b+c,e)
        if os<oe:
          new.append((os-b+a, oe-b+a))
          if s < os:
            seeds.append((s, os))
          if oe < e:
            seeds.append((oe, e))
          break
      else:
        new.append((s,e))
    seeds = new
  print(min(seeds)[0])
part2(inputs, others)

# def foo(inputs, others):
#   def f(R, o):
#     A = []
#     for line in o:
#       dest, src, sz = [int(x) for x in line.split()]
#       src_end = src+sz
#       NR = []
#       while R:
#         (st, ed) = R.pop()
#         before = (st, min(ed, src))
#         inter = (max(st, src), min(src_end, ed))
#         after = (max(src_end, st), ed)
#         if before[1]>before[0]:
#           NR.append(before)
#         if inter[1]>inter[0]:
#           A.append((inter[0]-src+dest, inter[1]-src+dest))
#         if after[1]>after[0]:
#           NR.append(after)
#       R = NR
#     return A+R
  
#   S = []
#   si = 0
#   while si< len(inputs):
#     st, sz = int(inputs[si]), int(inputs[si+1])
#     si += 2
#     R = [(st, st+sz)]
#     for o in others:
#       O = o.split('\n')
#       R = f(R, O[1:])
#       S.append(min(R)[0])
#   print(min(S))

# # foo(seed, others) 