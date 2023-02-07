from ast import Return


class Node:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right


    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
               if self.right is None:
                  self.right = Node(val)
               else:
                  self.right.insert(val)
        else:
            self.val = val

    # ledt - root - right
    def inorder(self,root):
        stack=[]
        if root==None:
            return None
        if root:
            self.inorder(root.left)
            stack.append(root.val)
            self.inorder(root.right)
        return stack

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val),
        if self.right:
            self.right.printTree()



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorder(root))

'''
Two type of taversal:
1) DFS
    1) pre-order = root-left-right
    2) in-order = left-root-right
    3) post-order = left-right-root

2) BFS
    1) level-order = level by level
'''