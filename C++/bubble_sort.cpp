#include <iostream>
using namespace std;

int printarr(int *arr,int n);
int bubble(int *arr,int n);

int main() {
    int size, m=0;
    cout<< "Enter the number of elements you want: ";
    cin>>size;

    int A[size];
    for(m=0; m<size; m++){
        cout<<"Enter the element number "<<m+1<<": ";
        cin>>A[m];
    }

    cout<<"Array before sorting\n\n";
    printarr(A, size);
    cout<<"Array after sorting\n\n";
    bubble(A,size);
    printarr(A,size);
    return 0;
}

int printarr(int *arr, int n){
    int i=0;
    for(i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
}

int bubble(int *arr,int n){
    int i=0, j=0, temp;
    for(i=0; i<n; i++){
        for(j=0; j<n-i-1; j++){
            if(arr[j]>arr[j+1]){
                temp= arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}