dx = [1,-1,1,-1,2,2,-2,-2]
dy = [2,2,-2,-2,1,-1,1,-1]

tmp = list(input())
# print(tmp)
x=int(tmp[1])
y=ord(tmp[0])-96
# print(x,y)
count=0
for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if (nx<1 or nx>8 or ny<1 or ny>8):
        continue
    count+=1

print(count)