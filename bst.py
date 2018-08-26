class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    def height(self,node):
        if node == None:
          return 0
        else:
          lheight = self.height(node.l)
          rheight = self.height(node.l)
          if lheight > rheight:
            return 1+lheight
          else:
            return 1+rheight

    def insert(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._insert(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._insert(val, node.r)
            else:
                node.r = Node(val)
    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return True
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)
    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None
    def Inorder(self,root):##problem
        if (root):
            self.Inorder(root.l)
            print(root.v)
            self.Inorder(root.r)
    def Preorder(self,root):
        if (root):
            print(root.v)
            self.Preorder(root.l)
            self.Preorder(root.r)
            
    def Postorder(self,root):
        if (root):
            self.Postorder(root.l)
            self.Postorder(root.r)
            print(root.v)
    def BFS(self,root):
      if root is None:
          return
      queue = []
      queue.append(root)
  
      while(len(queue) > 0):
          print(queue[0].v)
          node = queue.pop(0)
          if node.l is not None:
              queue.append(node.l)
          if node.r is not None:
              queue.append(node.r)
    def numnodes(self,root):
      if root == None:
        return 0
      else:
        left = self.numnodes(root.l)
        right = self.numnodes(root.r)
        return (1+left+right)
    def isBST(self,root):
      mini = float('-inf')
      maxi = float('inf')
      self.isbst(root,mini,maxi)
      
    def isbst(self,root,mini,maxi):
      if(root == None):
        return 1
      elif(root.v <= mini or root.v > maxi):
        return -1
      return(self.isbst(root.l,mini,root.v) and self.isbst(root.r,root.v,maxi))
    def minnode(self,root):
      curr = root
      while(curr.l is not None):
        curr = curr.l
      return curr.v
    def maxnode(self,root):
      curr = root
      while(curr.r is not None):
        curr = curr.r
      return curr.v
    def lca(self,root,n1,n2):
      if(root == None):
        return None
      if(root.v > n1 and root.v > n2):
        return self.lca(root.l,n1,n2)
      elif(root.v < n1 and root.v < n2):
        return self.lca(root.r,n1,n2)
      return root.v
    def delete(self,root,key):
      if root is None:
        return root
      if key < root.v:
        root.l = self.delete(root.l, key)
      elif key > root.v:
        root.r = self.delete(root.r, key)
      else:
        if root.l is None :
            temp = root.r 
            root = None
            return temp 
             
        elif root.r is None :
            temp = root.l 
            root = None
            return temp

        temp = self.minnode(root.r)
        root.v = temp.v
        root.r = self.delete(root.r,temp.v)
      return root

tree = Tree()
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(7)
tree.Inorder(tree.getRoot())
tree.delete(tree.getRoot(),1)
tree.Inorder(tree.getRoot())