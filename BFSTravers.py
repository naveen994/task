import queue
def bfs(matrix,u,visited):
    q=queue.Queue()
    q.put(u)
    while not q.empty():
        u=q.get()
        print(u,end=' ')
        visited[u]=True
        for i in range(v):
            if matrix[u][i]>0 and visited[i] is False:
                q.put(i)
                visited[i]=True

v,e=[int(i) for i in input().strip().split(' ')]
matrix=[[0 for i in range(v)] for j in range(v)]
for i in range(e):
    a,b=input().split(' ')
    aval=int(a)
    bval=int(b)
    matrix[aval][bval]=1
    matrix[bval][aval]=1
visited=[False for i in range(v)]
for i in range(v):
    if visited[i]==False:
        bfs(matrix,i,visited)
