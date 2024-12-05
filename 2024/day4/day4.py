with open("input.txt") as f:
    # data = f.readlines()
    data = f.read().strip().split('\n')

rows = len(data)
cols = len(data[0])
p2 = 0
ans = 0
for r in range(rows):
    for c in range(cols):
        if c+3<cols and data[r][c]=='X' and data[r][c+1]== 'M' and data[r][c+2]== 'A' and data[r][c+3]=='S':
            ans+=1
        if r+3<rows and data[r][c]=='X' and data[r+1][c]== 'M' and data[r+2][c]== 'A' and data[r+3][c]=='S':
            ans+=1
        if c+3<cols and data[r][c]=='S' and data[r][c+1]== 'A' and data[r][c+2]== 'M' and data[r][c+3]=='X':
            ans+=1
        if r+3<rows and data[r][c]=='S' and data[r+1][c]== 'A' and data[r+2][c]== 'M' and data[r+3][c]=='X':
            ans+=1
        if r+3<rows and c+3<cols and data[r][c]=='X' and data[r+1][c+1]=='M' and data[r+2][c+2]=='A' and data[r+3][c+3]=='S':
            ans+=1
        if r-3>=0 and c+3<cols and data[r][c]=='X' and data[r-1][c+1]=='M' and data[r-2][c+2]=='A' and data[r-3][c+3]=='S':
            ans+=1
        if r-3>=0 and c+3<cols and data[r][c]=='S' and data[r-1][c+1]=='A' and data[r-2][c+2]=='M' and data[r-3][c+3]=='X':
            ans+=1
        if r+3<rows and c+3<cols and data[r][c]=='S' and data[r+1][c+1]=='A' and data[r+2][c+2]=='M' and data[r+3][c+3]=='X':
            ans+=1

        if r+2<rows and c+2<cols and data[r][c]=='M' and data[r+2][c]=='M' and data[r][c+2]=='S' and data[r+1][c+1]=='A' and data[r+2][c+2]=='S':
            p2+=1  
        if r+2<rows and c+2<cols and data[r][c]=='S' and data[r+2][c]=='M' and data[r][c+2]=='S' and data[r+1][c+1]=='A' and data[r+2][c+2]=='M':
            p2+=1  
        if r+2<rows and c+2<cols and data[r][c]=='M' and data[r+2][c]=='S' and data[r][c+2]=='M' and data[r+1][c+1]=='A' and data[r+2][c+2]=='S':
            p2+=1  
        if r+2<rows and c+2<cols and data[r][c]=='S' and data[r+2][c]=='S' and data[r][c+2]=='M' and data[r+1][c+1]=='A' and data[r+2][c+2]=='M':
            p2+=1  
print(ans)
print(p2)