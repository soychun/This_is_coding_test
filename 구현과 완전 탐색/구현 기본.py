# 2차원 공간은 matrix, 행렬의 의미로 사용되고, 구현 문제에서 일반적으로 많이 사용된다

# 시뮬레이션 및 완전탐색 문제에서는 2차원 공간에서의 방향벡터가 자주 활용된다
#동, 북, 서, 남
dx = [0,-1,0,1]  #행이 x
dy = [1,0,-1,0]
x,y = 2,2
for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    print(nx,ny)