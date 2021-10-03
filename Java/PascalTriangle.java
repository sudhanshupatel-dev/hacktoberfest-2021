import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	System.out.println("Enter Number of rows: "); //messageto ask for rows
		Scanner scanner = new Scanner(System.in); //initialize scanner
        int x = scanner.nextInt(); //get rows count
        scanner.close();
        int a[][] = new int [x][x];
        for (int i=0; i<x; i++) {
            a[i][0] = 1;
            for (int j=0; j<i; j++) {
                a[i][j+1] = a[i-1][j] + a[i-1][j+1];
            }
            a[i][i] = 1;
        } 
        String s = "";
        for (int i=1; i<x+1; i++) {
            s += new String(new char[a.length-i]).replace("\0", "  ");
            for (int j=0; j<i; j++) {
                s += a[i-1][j] + "   ";
            }
            s += "\n";
        } 
        System.out.println(s);
    }
}