import java.lang.Math;

public class ProjectEuler1 {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        int multiSum = multiplesSum(3, 5, 999);
        long endTime = System.currentTimeMillis();
        long elapsedTime = endTime - startTime;
        System.out.println("Multiples sum: " + multiSum);
        System.out.println("Elapsed time: " + elapsedTime + " ms");
    }

    public static int multiplesSum(int a, int b, int upperBound) {
        int c = a * b;
        int aSum = (int) (Math.floor(upperBound / a) * (a + Math.floor(upperBound / a) * a) / 2);
        int bSum = (int) (Math.floor(upperBound / b) * (b + Math.floor(upperBound / b) * b) / 2);
        int cSum = (int) (Math.floor(upperBound / c) * (c + Math.floor(upperBound / c) * c) / 2);
        return aSum + bSum - cSum;
    }
}