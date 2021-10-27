#include <iostream>
#include<string>
#include <cmath>
#include<ctime>
#include<bits/stdc++.h> 
using namespace std;

void palindrome_product(int upper_bound) {
  int largest_palindrome = 0;
    for (int x = 102; x < upper_bound; x++){
        for (int y = 100; y < x; y++){
            int reversed = 0, placeholder = x*y;
            while(placeholder > 0){
                reversed = reversed*10 + placeholder%10;
                placeholder /= 10;}
            if (x*y == reversed){
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
