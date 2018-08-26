class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    def sizeoflist(self):
        temp = self.head
        count = 0
        while(temp):
          count += 1
          temp = temp.next
        return count
    def isempty(self):
      if(self.head == None):
        print(True)
      else:
        print(False)
    def valueatindex(self,key):
      temp = self.head
      index = 0
      while(temp):
        if(index == key):
          return(temp.data)
        index += 1
        temp = temp.next
    def pushfront(self,element):
      element = Node(element)
      element.next = self.head
      self.head = element
    def pushback(self,element):
      element = Node(element)
      if(self.head == None):
        element = self.head
        return
      temp = self.head
      while(temp.next):
        temp = temp.next
      temp.next = element
    def insertatindex(self,index,new_data):
      new_data = Node(new_data)
      size = self.sizeoflist()
      if(index == 0):
        new_data.next = self.head
        self.head = new_data
      else:
        if(index > size ):
          index = size
        previous = index -1
        temp = self.head
        count = 0
        while(temp):
          if(count == previous):
            new_data.next = temp.next
            temp.next = new_data
            return
          count += 1
          temp = temp.next
    def eraseatindex(self,index):
        temp = self.head
        if(index == 0):
          self.head = temp.next
          return
        else:
          count = 0
          while(temp):
            if(count == index-1):
              temp.next = temp.next.next
            count += 1
            temp = temp.next
    def popback(self,size):
      temp = self.head
      count = 0
      while(temp):
        if(count == size-2):
          temp.next = None
          return
        temp = temp.next
        count += 1
    def popfront(self):
      temp = self.head
      if(temp == None):
        print("List already empty")
        return
      temp2 = temp.next
      temp.next = None
      self.head = temp2
    def front(self):
      temp = self.head
      if(temp == None):
        print("Empty List")
        return
      else:
        return temp.data
    def back(self):
      size = self.sizeoflist()
      temp = self.head
      count = 0
      if(temp == None):
        print("Empty List")
        return
      while(temp):
        if(count == size-1):
          print(temp.data)
          return
        temp = temp.next
        count += 1
    def valuefromend(self,index):
      size = self.sizeoflist()
      index = size- index-1
      print(self.valueatindex(index))
    def reverse(self):
      curr = self.head
      prev = succ = None
      while(curr):
        succ = curr.next
        curr.next = prev
        prev = curr
        curr = succ
      self.head = prev
    ##Floyd’s Cycle-Finding Algorithm
    def detectloop(self):  
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print ("Found Loop")
                return
        print("No Loop")
    def swapNodes(self, x, y):
 
        # Nothing to do if x and y are same
        if x == y:
            return
 
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
 
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
 
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else: #make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else: # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
    def middle(self):
      slow_p = self.head
      fast_p = self.head
      while(fast_p.next != None and fast_p.next.next != None):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
      print(slow_p.data)
    def remove(self,value):
      temp = self.head
      prev = None
      if (temp is not None):
            if (temp.data == value):
                self.head = temp.next
                temp = None
                return
      while(temp):
        if(temp.data == value):
          prev.next = temp.next
          return
        prev = temp
        temp = temp.next


      
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
    slist = LinkedList()
    llist.head  = Node(1)
    second = Node(2)
    third  = Node(3)
    llist.head.next = second
    second.next = third
    third.next = None
    llist.pushback(4)
    llist.pushfront(0)
  
    
