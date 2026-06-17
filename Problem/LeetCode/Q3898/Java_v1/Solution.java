/* 
public int[]로 선언했으므로 return의 대상이 int[]의 형태여야 한다
*/

class Solution {
    public int[] findDegrees(int[][] matrix) {
        int[] ans = new int[matrix.length];

        for(int i = 0; i < matrix.length; i++){
            int sum = 0;
            for(int j = 0; j < matrix[i].length; j++){
                sum += matrix[i][j];
            }
            ans[i] = sum;
        }

        return ans;
    }
}