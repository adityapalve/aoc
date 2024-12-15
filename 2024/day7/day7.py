with open('input.txt') as f:
  data = f.read().strip().split('\n')
p1 = 0
p2 = 0

def is_valid(target, ns, p2):
  if len(ns) == 1:
    return ns[0] == target
  if is_valid(target, [ns[0]+ns[1]]+ns[2:], p2):
    return True
  if is_valid(target, [ns[0]*ns[1]]+ns[2:], p2):
    return True
  if p2 and is_valid(target,[int(str(ns[0])+str(ns[1]))] + ns[2:], p2): 
    return True
  return False 

for lines in data:
  test_val, l = lines.split(':')
  target = int(test_val)
  nums = list(map(int, l.strip().split(' ')))

  # ops = ['*','+']
  # for i in range(nums):
  #   for 
  if is_valid(target, nums, p2=False):
    p1+=target
  if is_valid(target, nums, p2=True):
    p2+=target
  
print(p1)
print(p2)