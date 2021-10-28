#include <iostream>
#include<ctime> 
using namespace std;
int pythagorean_triplet(int upper_bound){
    for(int x=1; x < 1000; x++){
        for(int y=1; y < 1000; y++){
            int z = upper_bound - x - y;
            if(x*x + y*y == z*z){
                cout << x << endl;
                cout << y << endl;
                cout << z << endl;
                return 0;
                
            }
        }
    }

}
int main()
{
    int start_s=clock() ;
    pythagorean_triplet(1000);
    int stop_s=clock();
    cout<<(stop_s-start_s)/double(CLOCKS_PER_SEC);
}
