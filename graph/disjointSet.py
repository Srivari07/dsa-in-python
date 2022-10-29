class DisjointSet:
    rank=[]
    parent=[]

    def __init__(self, n) -> None:
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(0,n+1)]

    def findParent(self, node):
        if node==self.parent[node]:
            return node

        self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        ulp_u=self.findParent(u)
        ulp_v=self.findParent(v)

        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v

        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u

        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=1

obj=DisjointSet(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)
# print(obj.rank)
# print(obj.parent)
if obj.findParent(4) == obj.findParent(0):
    print('Yes')
else:
    print('No')
if obj.findParent(1) == obj.findParent(0):
    print('Yes')
else:
    print('No')
        