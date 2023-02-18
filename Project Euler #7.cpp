#include <iostream>
#include <cmath>
#include <vector>
#include <ctime>
#include <numeric>
#include <chrono>


double f(double x) {
    return x / log(x) - 10001;}


double f_prime(double x) {
    return (log(x) - 1) / pow(log(x), 2);}


double newton_raphson(double x0, double tol) {
    double x = x0;
    double fx = f(x);
    while (abs(fx) > tol) {
        double fprime_x = f_prime(x);
        if (fprime_x == 0) {
            std::cout << "Error: derivative is zero.\n";
            return 0;}
        x = x - fx / fprime_x;
        fx = f(x);}
    return x;}


int prime_finder(int number) {
    std::vector<int> primelist = { 2 };
    int* prime = new int[number + 1] {};
    std::fill_n(prime, number + 1, 1);
    for (int y = 3; y < std::sqrt(number + 1); y += 2) {
        if (prime[y] == 1) {
            for (int x = y * y; x < number + 1; x += y + y) {
                prime[x] = 0;}}}
    for (int x = 3; x < number + 1; x += 2) {
        if (prime[x] == true) {
            primelist.push_back(x);}}
    return primelist[10000]; }


int main() {
    double x0 = 10001.0;
    double tol = 1e-6;
    double root = newton_raphson(x0, tol);
    int upper_bound = static_cast<int>(root);
    auto start_time = std::chrono::high_resolution_clock::now();
    int prime_no_10001 = prime_finder(upper_bound);
    std::cout << prime_no_10001 << std::endl;
    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time).count();
    std::cout << "Time taken by loop: " << duration << " seconds" << std::endl;
    return 0;}
