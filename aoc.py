s = """11   15458   2293  ****
10   29110  14295  ********
 9   55551    760  **********
 8   57140  11593  ***********
 7   65286   5766  ***********
 6   84197   1354  **************
 5   66452  25824  ***************
 4  109768  14502  ********************
 3  111075  16509  ********************
 2  168709   7605  ****************************
 1  201015  63514  *****************************************"""

for x in s.splitlines():
  nums = list(map(int,x.split()[1:3]))
  n = [int(i) for i in x.split()[1:3]]
  print(n)