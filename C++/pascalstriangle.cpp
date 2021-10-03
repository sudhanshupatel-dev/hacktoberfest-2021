#include<bits/stdc++.h>
using namespace std;
 
int main()
{
    int rows;
    cout << "Enter the number of rows : ";
    cin >> rows;
    cout << endl;
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < v[i].size(); j++){
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
