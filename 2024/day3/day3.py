import re
test = 'test.txt'
input = 'input.txt'

with open(input) as f:
  data = f.readlines()

def process_line(line):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, line)
    total = 0
    
    for match in matches:
      num1 = int(match.group(1))
      num2 = int(match.group(2))
      total += num1 * num2
    
    return total

def scan(line):
    line = line.strip().replace('\n', '')
    total = 0
    i = 0
    flag = True 
    while i < len(line):
      # do(), don't()
      # if line[i] == 'd':
      if i+4 < len(line) and line[i:i+4] == 'do()':
        flag = True
        i += 4
        continue
        
      if i+7 < len(line) and line[i:i+7] == "don't()":
        flag = False
        i += 7 
        continue

      if line[i] == 'm':
        if i + 3 < len(line) and line[i:i+3] == 'mul' and line[i+3] == '(':
          i += 4  
          num1 = ''
          while i < len(line) and line[i].isdigit():
            num1 += line[i]
            i += 1

          if i < len(line) and line[i] == ',':
            i += 1  
            num2 = ''
            while i < len(line) and line[i].isdigit():
              num2 += line[i]
              i += 1
            
            if i < len(line) and line[i] == ')':
              if num1 and num2 and flag:  
                total += int(num1) * int(num2)
              continue
            
      i += 1
    
    return total


def part1():
  ans = 0
  for line in data:
    ans += scan(line)
  return ans
  
print(part1())