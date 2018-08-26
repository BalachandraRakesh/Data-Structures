#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
};

class linked_list
{
private:
    node *head,*tail;
public:
    linked_list()
    {
        head = NULL;
        tail = NULL;
    }

    void add_node(int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = NULL;

        if(head == NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
    
    }

    void display()
    {
        node *tmp = new node;
        tmp = head;
        while (tmp != NULL)
        {
            cout << tmp->data << endl;
            tmp = tmp->next;
        }
    }
    void pushfront(int n)
    {
        node *tmp = new node;
        tmp -> data = n;
        tmp -> next = head;
        head = tmp;
    }
    void pushback(int n)
    {
      node *tmp = new node;
      tmp->data = n;
      tail->next = tmp;
      tail = tmp;
    }
    int sizeoflist()
    {
      node *tmp = new node;
      tmp = head;
      int count = 0;
      while(tmp != NULL){
        count += 1;
        tmp = tmp->next;
      }
      return count;
    }
    bool isempty()
    {
      node *tmp = new node;
      tmp = head;
      if(tmp == NULL){
        return true;
      }
      else{
        return false;
      }
    delete(tmp);
    }
    int valueatindex(int n)
    {
      node *tmp = new node;
      tmp = head;
      int count = 0;
      while(tmp)
      {
        if(count == n){
          return tmp->data;
        }
        tmp = tmp->next;
        count += 1;
      }
    delete(tmp);
    }
    void insertatindex(int index,int value){
      node *tmp = new node;
      tmp->data = value;
      int prev = index - 1;
      node *tmp1 = new node;
      tmp1 = head;
      int count = 0;
      while(tmp1){
        if(count == prev){
          tmp->next = tmp1->next;
          tmp1->next = tmp;
          return;
        }
        count += 1;
        tmp1 = tmp1->next;
      }
    }
    void deleteatindex(int index){
      node *tmp = new node;
      tmp = head;
      int prev = index - 1;
      int count = 0;
      while(tmp){
        if(count == prev){
          tmp->next = tmp->next->next;
          return;
        }
        count += 1;
        tmp = tmp->next;
      }
    }
    int valuefromend(int index){
      int size = sizeoflist();
      index = size - index ;
      cout << valueatindex(index) << endl;
      return 0; 
    }

};

int main()
{
    linked_list a;
    linked_list b;
    a.add_node(1);
    a.add_node(2);
    a.pushfront(0);
    a.pushback(3);
    a.display();
    
    return 0;
}