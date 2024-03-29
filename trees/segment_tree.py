
class SegmentTree:
    def __init__(self,arr) -> None:
        self.n=len(arr)
        self.tree = [0]*(4*self.n)    # SC:O(4n)
        self.build(arr,0,0,self.n-1)

    # node = idx of node in tree [0 to 4n]
    def build(self,arr,node,start,end):
        # at leaf node
        if start==end:
            self.tree[node]=arr[start]
            return

        mid=(start+end)//2

        # left side
        self.build(arr,2*node+1,start,mid)

        # right side
        self.build(arr,2*node+2,mid+1,end)

        # add left and right
        self.tree[node]=self.tree[2*node+1]+self.tree[2*node+2]
    
    def query(self, node, start, end,l,r):
        # not in range
        if start > r or end < l:
            return 0
        # in range
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) // 2

        leftSide = self.query(2 * node+1, start, mid, l, r)
        rightSide = self.query(2 * node+2, mid + 1, end, l, r)

        return leftSide+rightSide

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node+1, start, mid, idx, value)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, value)
        self.tree[node]=self.tree[2*node+1]+self.tree[2*node+2]

arr=[1,3,5]
n=len(arr)
node=0 # idx of node
start=0
end=n-1

st=SegmentTree(arr)
print(st.query(node,start,end,1,3)) # 8
st.update(node,start,end,2,3)
print(st.query(node, start, end, 1, 3)) # 7

'''
Time Complexities:
    Tree Construction: O(n)
    Query in Range: O(Log n)
    Updating an element: O(Log n)

Auxiliary Space: O(2*N)/O(4n)
'''
