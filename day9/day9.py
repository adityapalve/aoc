with open("input.txt") as f:
  s = f.read()
lines = s.strip().split('\n')
# for x in s.strip().split('\n'):
#   nums = x.split()
#   diff = [int(nums[x])-int(nums[x-1]) for x in range(1,len(nums))]

def f(xs, part2):
  D = []
  for i in range(len(xs)-1):
    D.append(xs[i+1]-xs[i])
  if all(y==0 for y in D):
    return xs[0] 
  else:
    return xs[0 if part2 else -1] + (-1 if part2 else 1)*f(D,part2)

for part2 in [True]:
  ans = 0
  for line in lines:
    xs = [int(x) for x in line.split()]
    # print(xs)
    ans += f(xs, part2)
  print(ans)