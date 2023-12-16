with open("input.txt") as f:
  s = f.read().strip()

steps = s.split(',')
def hashing(s):
  val = 0 
  for c in s:
    val = ((val+ord(c))*17)%256
  return val

box = [[] for _ in range(256)]
for step in steps:
  if step[-1] == "-":
    name = step[:-1]
    h = hashing(name)
    box[h] = [(n,v) for (n,v) in box[h] if n!= name]
  elif step[-2] == "=":
    name = step[:-2]
    l = int(step[-1])
    h = hashing(name)
    if name in [n for (n,v) in box[h]]:
      box[h] = [(n,l if name==n else v) for (n,v) in box[h]]
    else:
      box[h].append((name,l))
  # print(box[hashing(step[:2])])

count = 0
for j, b in enumerate(box):
  if b != []:
    print(b)
  for i, (n,v) in enumerate(b):
    fp = (1+j)*(i+1)*v
    print(fp, (1+j), i+1,v)
    count += fp
print(count)
  