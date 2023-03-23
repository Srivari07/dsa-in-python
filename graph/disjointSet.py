class DisjointSet:
    parent=[]
    size=[]
    rank=[]

    def __init__(self, n) -> None:
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
        self.rank=[0]*(n+1)

    def findParent(self, node):
        if node==self.parent[node]:
            return node

        self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self,u,v):
        ulp_u=self.findParent(u)
        ulp_v=self.findParent(v)

        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v

        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u

        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=1
    
    def unionBySize(self, u, v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)

        if ulp_u==ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

obj=DisjointSet(5)
# obj.unionByRank(0, 2)
# obj.unionByRank(4, 2)
# obj.unionByRank(3, 1)

obj.unionBySize(0, 2)
obj.unionBySize(4, 2)
obj.unionBySize(3, 1)
# print(obj.rank)
# print(obj.size)
# print(obj.parent)
if obj.findParent(4) == obj.findParent(0):
    print('Yes')
else:
    print('No')
if obj.findParent(1) == obj.findParent(0):
    print('Yes')
else:
    print('No')
        
