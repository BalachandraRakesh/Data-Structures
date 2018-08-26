##Splay Trees
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def root(self):
        return self.root
    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return Node(key)

        self.root = self.splay(self.root,key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
          
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
            
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.root = self.splay(self.root,key)
        if key != self.root.key:
            raise 'key not found in tree'

        # Now delete the root.
        if self.root.left== None:
          x = self.root
          self.root = self.root.right
        else:
            x = self.root
            self.root = self.splay(self.root.left,key)
            self.root.right = x
            self.root.right = x.right
    

    def search(self, key):
        if self.root == None:
            return None
        self.root = self.splay(self.root,key)
        if self.root.key != key:
            print("Not present")
            return None
        return self.root
      

    def isEmpty(self):
        return self.root == None

    def Preorder(self,root):
        if (root):
            print(root.key)
            if(root.left is not None):
              self.Preorder(root.left)
            if(root.right is not None):
              self.Preorder(root.right)
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y
    def rightRotate(self, z):
    
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y
    def splay(self,root,key):
      if(root == None or root.key == key):
        return root
      if(key < root.key):
        if(root.left == None):
          return root
        if(key < root.left.key):
          root.left.left = self.splay(root.left.left,key)
          root = self.rightRotate(root)
        elif(key > root.left.key):
          root.left.right = self.splay(root.left.right,key)
          if(root.left.right is not None):
            root.left = self.leftRotate(root.left)
        if(root.left is not None):
          root = self.rightRotate(root)
          return root
        else:
          return root
      else:
        if(root.right == None):
          return root
        if(key > root.right.key):
          root.right.right = self.splay(root.right.right,key)
          root = self.leftRotate(root)
        elif(key < root.right.key):
          root.right.left = self.splay(root.right.left,key)
          if(root.right.left is not None):
            root.right = self.rightRotate(root.right)
        if(root.right is not None):
          root = self.leftRotate(root)
          return root
        else:
          return root

tree = SplayTree()
tree.insert(100)
tree.insert(50)
tree.insert(200)
tree.insert(40)
tree.insert(30)
tree.insert(20)
tree.insert(25)
tree.Preorder(tree.root)

