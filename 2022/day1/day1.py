with open("input.txt") as f:
    s = f.read().strip().split('\n\n')

ans = [] 
for elves in s:
    cals = list(map(int, elves.split('\n')))
    ans.append(sum(cals))
ans = sorted(ans, reverse=True)[:3]
print(sum(ans))
