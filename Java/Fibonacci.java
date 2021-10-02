import java.util.Scanner;
class Fibonacci 
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
Fibonacci obj=new Fibonacci();
System.out.println("Enter number of terms : ");
int n=sc.nextInt();
System.out.println();
for(int i=1;i<=n;i++)
{
int f=obj.fib(i);
System.out.print(f+ " ");
}
}
public int fib(int n)
{
if(n<=1)
return n;
else
return (fib(n-1)+fib(n-2));
}
}
