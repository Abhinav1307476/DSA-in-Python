#include<bits/stdc++.h>
using namespace std;
class Stack{
public:
    int bottom;
    int top;
    int max_size;
    vector<int> stack;

    Stack(int max_size){
        bottom=0;
        top=-1;
        this->max_size=max_size;
        stack.resize(max_size);
    }

    bool is_empty(){
        return top==-1;
    }

    bool is_full(){
        return top+1>=max_size;
    }

    void push(int data){
        if(is_full()){
            cout<<"Stack is full"<<endl;
            return;
        }
        for(int i=top;i>=0;i--){
            stack[i+1]=stack[i];
        }
        stack[bottom]=data;
        top++;
    }

    int pop(){
        if(is_empty()){
            cout<<"Stack is empty"<<endl;
            return -1;
        }
        int item=stack[bottom];
        for(int i=bottom;i<top;i++){
            stack[i]=stack[i+1];
        }
        top--;
        return item;
    }

    int peek(){
        if(is_empty()){
            cout<<"Stack is empty"<<endl;
            return -1;
        }
        return stack[bottom];
    }
};

int main(){
    int max_size;
    cin>>max_size;
    Stack s(max_size);
    cout << "Is the stack empty? " << s.is_empty() << endl;
    cout << "Is the stack full? " << s.is_full() << endl;

    cout << "Pop from the stack: " << s.pop() << endl;
    // This will print a message since the stack is empty

    cout << "Peek at the top element: " << s.peek() << endl;
    // This will print a message since the stack is empty

    s.push(10);

    cout << "Peek at the top element after pushing 10: "<< s.peek() << endl;

    cout << "Is the stack empty? " << s.is_empty() << endl;
    cout << "Is the stack full? " << s.is_full() << endl;

    s.push(20);

    cout << "Peek at the top element after pushing 20: "<< s.peek() << endl;

    s.push(30);

    cout << "Peek at the top element after pushing 30: "<< s.peek() << endl;

    s.push(40);
    s.push(50);

    cout << "Peek at the top element after pushing 50: "<< s.peek() << endl;

    cout << "Is the stack empty? " << s.is_empty() << endl;
    cout << "Is the stack full? " << s.is_full() << endl;

    s.push(60);
    // This will print a message since the stack is full

    cout << "Pop from the stack: " << s.pop() << endl;
    cout << "Pop from the stack: " << s.pop() << endl;
    cout << "Pop from the stack: " << s.pop() << endl;
    cout << "Pop from the stack: " << s.pop() << endl;

    cout << "Is the stack empty? " << s.is_empty() << endl;

    cout << "Peek at the top element: " << s.peek() << endl;

    cout << "Pop from the stack: " << s.pop() << endl;

    cout << "Is the stack empty? " << s.is_empty() << endl;

    cout << "Peek at the top element: " << s.peek() << endl;
    return 0;
}