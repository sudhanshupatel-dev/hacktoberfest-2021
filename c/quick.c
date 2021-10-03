#include <stdio.h>
void quick(int a[],int p,int r);
int part(int a[],int p,int r);

void main(){
    int a[100],i,p,r,n;
    printf("Enter the number:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d", &a[i]);
    }
   
    quick(a,0,n-1);
    for(i=0;i<n;i++)
    {
        printf("%d\n", a[i]);
    }
}
void quick(int a[],int p,int r){
    int q;
   if(p<r)
   {
     q=part(a,p,r);
     quick(a,p,q-1);
     quick(a,q+1,r);
   }
}
int part(int a[],int p,int r){
    int j,i,x,temp=0,swap=0 ;
    x=a[r];
    i=p-1;
    for(j=p;j<r;j++)
    {
        if(a[j]<=x)
        {
            i=i+1;
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
           
        }
    }
    swap=a[i+1];
    a[i+1]=a[r];
    a[r]=swap;
    return i+1;
}