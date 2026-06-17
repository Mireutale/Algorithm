import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        printResult("Example 1", solution.twoSum(new int[] {2, 7, 11, 15}, 9));
        printResult("Example 2", solution.twoSum(new int[] {3, 2, 4}, 6));
        printResult("Example 3", solution.twoSum(new int[] {3, 3}, 6));
    }

    private static void printResult(String label, int[] result) {
        System.out.println(label + ": " + Arrays.toString(result));
    }
}
