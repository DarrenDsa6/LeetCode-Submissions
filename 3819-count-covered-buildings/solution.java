import java.util.*;

class Solution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        Map<Integer, TreeSet<Integer>> rowMap = new HashMap<>();
        Map<Integer, TreeSet<Integer>> colMap = new HashMap<>();

        for (int[] b : buildings) {
            int x = b[0], y = b[1];
            rowMap.computeIfAbsent(x, k -> new TreeSet<>()).add(y);
            colMap.computeIfAbsent(y, k -> new TreeSet<>()).add(x);
        }

        int count = 0;
        for (int[] b : buildings) {
            int x = b[0], y = b[1];
            TreeSet<Integer> rowSet = rowMap.get(x);
            TreeSet<Integer> colSet = colMap.get(y);

            // Left = exists y < current in the same row
            // Right = exists y > current in the same row
            // Top = exists x < current in the same column
            // Bottom = exists x > current in the same column
            boolean hasLeft = rowSet.lower(y) != null;
            boolean hasRight = rowSet.higher(y) != null;
            boolean hasTop = colSet.lower(x) != null;
            boolean hasBottom = colSet.higher(x) != null;

            if (hasLeft && hasRight && hasTop && hasBottom) {
                count++;
            }
        }

        return count;
    }
}

