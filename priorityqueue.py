class maxheap:
  def __init__(self):
      #self.maxsize = data
      self.heap = []
      self.size = -1
  def parent(self,i):
    return(int((i-1)/2))
  def leftchild(self,i):
    return 2*i + 1
  def rightchild(self,i):
    return 2*i + 2
  def siftup(self,i):
    while (i > -1) and (self.heap[i] > self.heap[self.parent(i)]):
      self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]
      i = self.parent(i)
  def siftdown(self,i):
    maxindex = i
    l = self.leftchild(i)
    if(l < self.size and self.heap[l] > self.heap[maxindex]):
      maxindex = l
    r = self.rightchild(i)
    if(r < self.size and self.heap[r] > self.heap[maxindex]):
      maxindex = r
    if (i != maxindex ):
      self.heap[i],self.heap[maxindex] = self.heap[maxindex],self.heap[i]
      self.siftdown(maxindex)
  def extractmax(self):
    result = self.heap[0]
    self.heap[0] = self.heap[self.size]
    self.size = self.size -1
    self.siftdown(0) 
    return result
  def insert(self,p):
    #if (self.size == self.maxsize):
      #print("Error")
      #return
    self.size += 1
    self.heap.append(p)
    self.siftup(self.size)
  def remove(self,i):
    self.heap[i] = (float('inf'))
    self.siftup(i)
    self.extractmax()


h = maxheap()
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(1)
h.insert(12)
h.insert(22)
h.insert(47)
h.insert(9)
h.insert(9)
h.insert(17)
h.insert(109)
h.insert(32)
print(h.heap)
while(h.size >= 0 ):
  print(h.extractmax())





    

