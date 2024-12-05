import functools
with open('input.txt') as f:
    lblock, rblock = f.read().strip().split('\n\n')
    

order = lblock.split('\n')
updates = rblock.split('\n')
hash = {} 

for o in order:
    l, r = map(int, o.split('|'))
    hash[(l,r)] = -1
    hash[(r,l)] = 1

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            key = (update[i],update[j])
            if key in hash and hash[key] == 1:
                return False
    return True

def cmp(x,y):
    return hash.get((x,y), 0)

total = 0
for line in updates:
    update = list(map(int, line.split(',')))
    if is_ordered(update): continue
    update.sort(key=functools.cmp_to_key(cmp))
    total += update[len(update) // 2]

print(total)

def part1():
    for o in order:
        l, r = map(int, o.split('|'))
        if l in hash:
            hash[l].append(r)
        else:
            hash[l] = [r]
        
    s = 0
    for line in updates:
        line = list(map(int ,line.split(',')))
        flag = True
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[j] in hash.get(line[i],[]):
                    flag = True
                else:
                    flag = False
                    break

            if flag is False:
                break
        
        if flag is True:
            page = line[len(line)//2]
            s += page
    print(s)

part1()
