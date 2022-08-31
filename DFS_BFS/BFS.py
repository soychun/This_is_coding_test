# 너비 우선 탐색
# 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조를 이용,  그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 탐색 시작 노드를 큐에 삽입

from collections import deque

def bfs(graph,start,visited):
    queue = deque()
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited =[False]*9
bfs(graph,1,visited)
