import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        printResult("Example 1", solution.findDegrees(new int[][] {
            {0, 1, 1},
            {1, 0, 1},
            {1, 1, 0}
        }));
        printResult("Example 2", solution.findDegrees(new int[][] {
            {0, 1, 0},
            {1, 0, 0},
            {0, 0, 0}
        }));
        printResult("Example 3", solution.findDegrees(new int[][] {
            {0}
        }));
    }

    private static void printResult(String label, int[] result) {
        System.out.println(label + ": " + Arrays.toString(result));
    }
}
