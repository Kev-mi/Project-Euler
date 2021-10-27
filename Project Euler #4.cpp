#include <iostream>
#include<string>
#include <cmath>
#include<ctime>
#include<bits/stdc++.h> 
using namespace std;

void palindrome_product(int upper_bound) {
  int largest_palindrome = 0;
    for (int x = 100; x < upper_bound; x++){
        for (int y = 100; y < upper_bound; y++){
            string str_1 = to_string(x*y);
            string str_2 = to_string(x*y);
            reverse(str_2.begin(), str_2.end());
            if (str_1 == str_2){
                if (x*y > largest_palindrome){
                    largest_palindrome = x*y;
                }
            }
        }
    }
cout << largest_palindrome << endl;
}
int main()
{
    int start_s=clock() ;
    palindrome_product(1000);
    int stop_s=clock();
    cout<<(stop_s-start_s)/double(CLOCKS_PER_SEC);
    return 0;
}
