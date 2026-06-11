import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        printResult("Example 1", solution.isPalindrome(121));
        printResult("Example 2", solution.isPalindrome(-121));
        printResult("Example 3", solution.isPalindrome(10));
    }

    private static void printResult(boolean result) {
        System.out.println(result);
    }
}
