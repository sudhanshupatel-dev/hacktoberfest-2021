import java.util.*;
class Heap{
    int cap;
    int size;
    int arr[];
    Heap(int c){
        cap = c;
        arr = new int[cap];
        size = 0;
    }
    public void insert(int data){
        if(size == cap) return;
        size++;
        arr[size-1] = data;
        for(int i = size-1; i !=0 && arr[(i-1)/2] > arr[i];){
            int swap = arr[i];
            arr[i] = arr[(i-1)/2];
            arr[(i-1)/2] = swap;
            i = (i-1)/2;
        }
        
    }
    public void decreaseKey(int i,int newVal){
        if(i > size) return;
        arr[i] = newVal;
        while(i != 0 && arr[(i-1)/2] > arr[i]){
            int swap = arr[i];
            arr[i] = arr[(i-1)/2];
            arr[(i-1)/2] = swap;
            i = (i-1)/2;
        }
    }
    public void minHeapify(int i){
        int left = 2*i+1;
        int right = 2*i+2;
        int smallest = i;
        if(left < size && arr[left] < arr[i]) smallest = left;
        if(right < size && arr[right] < arr[smallest]) smallest = right;
        if(smallest != i){
            int swap = arr[i];
            arr[i] = arr[smallest];
            arr[smallest] = swap;
            minHeapify(smallest);
        }
        
    }
    public int extractMinimum(){
        if(size == 0) return Integer.MAX_VALUE;
        if(size == 1){
            size--;
            return arr[0];
        }
        int swap = arr[0];
        arr[0] = arr[size - 1];
        arr[size - 1] = swap;
        size--;
        minHeapify(0);
        return arr[size];
    }
    public void delete(int i){
        decreaseKey(i,Integer.MIN_VALUE);
        extractMinimum();
    }
    public void show(){
        for(int i = 0; i < size; i++){
            System.out.print(arr[i] + " ");
        }
    }
}
public class Main{
    public static void main(String[] args){
        Heap h = new Heap(8);
        h.insert(10);
        h.insert(20);
        h.insert(30);
        h.insert(40);
        h.insert(50);
        h.insert(35);
        h.insert(38);
        h.insert(45);
        h.show();
        h.delete(3);
        System.out.println();
        h.show();
    }
}
