#include <iostream>
#include <chrono>


int fibo_iter(int fibo_1, int fibo_2, int fibo_3, int even_fibo_sum) {
    for (int i = 1; i <= 100; i++) {
        if (fibo_1 + fibo_2 > 4000000) {
            break;}
        else {
            if (fibo_3 % 2 == 0) {
                even_fibo_sum = even_fibo_sum + fibo_3;}
            fibo_1 = fibo_2, fibo_2 = fibo_3, fibo_3 = fibo_1 + fibo_2;}}
    return even_fibo_sum;}


int main() {
    auto start_time = std::chrono::high_resolution_clock::now();
    int even_fibo_sum = fibo_iter(1, 1, 2, 0);
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
    std::cout << even_fibo_sum << "\n";
    std::cout << "Elapsed time: " << elapsed_time << " microseconds.\n";
    return 0;}
