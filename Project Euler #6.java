public class ProjectEuler6 {
    public static void main(String[] args) {
        int n = 100;
        long startTime = System.currentTimeMillis();
        int sum_of_squares = printNumbers(n);
        int sum_of_series = ((n+1)/2)*(n+1);
        int square_of_sum = (sum_of_series*sum_of_series);
        System.out.println(square_of_sum - sum_of_squares);
        long endTime = System.currentTimeMillis();
        System.out.println("Time taken: " + (endTime - startTime) + " ms");}

    public static int printNumbers(int n) {
        int sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6;
        return sum_of_squares;}}
