import java.util.Arrays;
import java.util.Vector;


public class PrimeFinder {
    public static void main(String[] args) {
        double x0 = 50001.0;
        double tol = 1e-6;
        int upper_bound = (int) solve(x0, tol);
        long startTime = System.currentTimeMillis();
        int selected_prime = primefinder(upper_bound);
        System.out.println(selected_prime);
        long endTime = System.currentTimeMillis();
        System.out.println("Time taken: " + (endTime - startTime) + " ms");}

    public static int primefinder(int num){
        Vector<Integer> primelist = new Vector<>();
        boolean[] primes = new boolean[num + 1];
        Arrays.fill(primes, true);
        primes[0] = primes[1] = false;
        for (int i = 3; i * i <= num; i += 2) {
            if (primes[i]) {
                for (int j = i * i; j <= num; j += i + i) {
                    primes[j] = false;}}}
        for (int i = 3; i <= num; i += 2) {
            if (primes[i]) {
                primelist.add(i);}}
        int count = primelist.size();
        int element = primelist.get(10001 - 2);
        return element;}

    public static double solve(double x0, double tol) {
        double x = x0;
        double fx = f(x);
        double dfx = df(x);
        while (Math.abs(fx) > tol) {
            x = x - fx / dfx;
            fx = f(x);
            dfx = df(x);}
        return (int) x;}

    public static double f(double x) {
        return x / Math.log(x) - 10001;}

    public static double df(double x) {
        return (1 / Math.log(x)) - (1 / Math.pow(Math.log(x), 2));}}

