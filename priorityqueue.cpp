#include <iostream>
#include <limits>
using namespace std;
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
class maxheap{
  public:
    int *heap; // pointer to array of elements in heap
    int maxsize; // maximum possible size of min heap
    int size; // Current number of elements in min heap
    maxheap(int data);
    int parent(int i){return (i-1)/2;}
    int leftchild(int i){return 2*i +1;}
    int rightchild(int i){return 2*i +2;}
    void insert(int i);
    void siftup(int i);
    void siftdown(int i);
    int extractmax();
    void remove(int i);
};
maxheap::maxheap(int data){
      maxsize = data;
      heap = new int[maxsize];
      size = -1;
}
void maxheap::siftup(int i){
  while(i > -1 && heap[parent(i)] < heap[i]){
    swap(&heap[parent(i)],&heap[i]);
    i = parent(i);
    }
}
void maxheap::insert(int i){
      if(size == maxsize){return;}
      size += 1;
      heap[size] = i;
      maxheap::siftup(size);
}
void maxheap::siftdown(int i){
    int maxindex = i;
    int l = leftchild(i);
    if(l < size && heap[l] > heap[i]){
      maxindex = l;
    }
    int r = rightchild(i);
    if(r < size && heap[r] > heap[i]){
      maxindex = r;
    }
    if(i != maxindex){
      swap(&heap[maxindex],&heap[i]);
      maxheap::siftdown(maxindex);
    }
}
int maxheap::extractmax(){
    int result = heap[0];
    heap[0] = heap[size];
    size = size-1;
    maxheap::siftdown(0);
    return result;
}
void maxheap::remove(int i){
  heap[i] = std::numeric_limits<int>::max();
  maxheap::siftup(i);
  maxheap::extractmax();
}
int main() {
  maxheap h(20);
  h.insert(2);
  h.insert(3);
  h.insert(4);
  h.insert(5);
  h.insert(1);
  h.insert(12);
  h.insert(22);
  h.insert(47);
  h.insert(9);
  h.insert(9);
  h.insert(17);
  h.insert(109);
  h.insert(32);
  for(int i = 0; i < h.size; i++){
    cout << h.heap[i] << endl;
  }

  

}