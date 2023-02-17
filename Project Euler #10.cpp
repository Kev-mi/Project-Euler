#include <iostream>
#include <cmath>
#include <vector>
#include <ctime>
#include <numeric>

long long prime_finder(int number) {
    std::vector<int> primelist = { 2 };
    int* prime = new int[number + 1] {};
    std::fill_n(prime, number + 1, 1);
    for (int y = 3; y < std::sqrt(number + 1); y += 2) {
        if (prime[y] == 1) {
            for (int x = y * y; x < number + 1; x += y + y) {
                prime[x] = 0;
            }
        }
    }
    for (int x = 3; x < number + 1; x += 2) {
        if (prime[x] == true) {
            primelist.push_back(x);
        }
    }
    long long sum = std::accumulate(primelist.begin(), primelist.end(), 0LL);
    return sum;}


int main()
{
    int upper_bound = 1999999;
    int start_s = clock();
    long long sum = prime_finder(upper_bound);
    std::cout << sum << std::endl;
    int stop_s = clock();
    std::cout << (stop_s - start_s) / double(CLOCKS_PER_SEC);
    return 0;
}
