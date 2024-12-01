with open('input.txt') as f:
    data = f.readlines()


def foo():
    left, right = [], []
    for line in data:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    s = 0
    # for l, r in zip(left, right):
    #     s = s + abs(l-r)
    # return s
    score = 0
    for l in left:
      freq = right.count(l)
      score = score + l*freq
    return score

print(foo())