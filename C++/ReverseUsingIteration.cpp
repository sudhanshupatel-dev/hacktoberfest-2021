#include<iostream>
using namespace std;

struct Node{
    int data;
    Node *next;
};
Node *head = NULL;
Node *end1 = NULL;
void Insert(int data){            //Time complexity = O(n) Space Complexity = O(1)
    Node *temp = new Node();
    temp -> data = data;
    temp -> next = NULL;
    if(head == NULL){
        head = temp;
        end1 = temp;
        return;        
    }
    end1 -> next = temp;
    end1 = temp;
}

void Reverse(){
    Node *temp = head;
    Node *current = head;
    Node *next1;
    Node *prev = NULL;
    while(current!= NULL){
        next1 = current -> next;
        current -> next = prev;
        prev = current;
        current = next1; 
    }
    head = prev; 
}
void Print(){
    Node *temp1 = head;
    while(temp1 != NULL){
        cout << temp1 -> data << " ";
        temp1 = temp1 -> next;
    }
   printf("\n"); 
}


int main(){
    Insert(21);
    Insert(32);
    Insert(45);
    Insert(23);
    Insert(5);
    Print();
    Reverse();
    Print();
}




