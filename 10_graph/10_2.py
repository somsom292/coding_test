def find_parent(parent,x):
    if parent[x]!=x:
        parent=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int, input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    method,a,b=map(int,input().split())
    if method==0:
        union_parent(parent,a,b)
    elif method==1:
        if find_parent(parent,a)==find_parent(parent,b):
            print('Yes')
        else:
            print('No')
