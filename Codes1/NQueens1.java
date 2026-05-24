import java.util.ArrayList;
import java.util.List;

class Solution {
    private int[] x;

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> solutions = new ArrayList<>();
        x = new int[n + 1]; 
        nQueen(1, n, solutions);
        return solutions;
    }

    private void nQueen(int k, int n, List<List<String>> solutions) {
        for (int i = 1; i <= n; i++) {
            if (place(k, i)) {
                x[k] = i;
                if (k == n) {
                    List<String> board = new ArrayList<>();
                    for (int j = 1; j <= n; j++) {
                        StringBuilder row = new StringBuilder();
                        for (int p = 1; p <= n; p++) {
                            if (x[j] == p) {
                                row.append("Q");
                            } else {
                                row.append(".");
                            }
                        }
                        board.add(row.toString());
                    }
                    solutions.add(board);
                } else {
                    nQueen(k + 1, n, solutions);
                }
            }
        }
    }

    private boolean place(int k, int i) {
        for (int j = 1; j < k; j++) {
            if ((x[j] == i) || (Math.abs(x[j] - i) == Math.abs(j - k))) {
                return false;
            }
        }
        return true;
    }
}
