test = 'test.txt'
input = 'input.txt'

with open(input) as f:
  data = f.readlines()


def part1():
  s = 0
  for line in data:
    check = False
    flag = True
    level = [int(x) for x in line.split()]
    # level = list(map(int, line.split())
    s_level = sorted(level)
    if (level == s_level) or (level[::-1] == s_level):
      # print(level, s_level)
      for i in range(1,len(level)):
        if abs(level[i] - level[i-1])<1 or abs(level[i] - level[i-1])>=4:
            flag = False
      # print(flag)
      if flag == True:
        s += 1
  return s


def check_sequence(level):
  if len(level) < 2:
    return True
  
  # Check if sequence is strictly increasing or decreasing with diff between 1 and 3
  flag = True
  for i in range(1, len(level)):
    if abs(level[i] - level[i-1]) < 1 or abs(level[i] - level[i-1]) >= 4:
      flag = False
  return flag


def foo():
  s = 0
  for line in data:
    level = [int(x) for x in line.split()]
    s_level = sorted(level)
    
    # Check if already safe without removing any number
    if (level == s_level or level[::-1] == s_level) and check_sequence(level):
      s += 1
      continue
        
    # Try removing each number once
    for i in range(len(level)):
      # Create new list without the i-th element
      new_level = level[:i] + level[i+1:]
      new_s_level = sorted(new_level)
      
      # Check if sequence is valid after removing element
      if (new_level == new_s_level or new_level[::-1] == new_s_level) and check_sequence(new_level):
        s += 1
        break
                
  return s


print(foo())