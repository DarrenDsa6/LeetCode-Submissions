public class Solution {
    public int[][] Merge(int[][] intervals) {
        Array.Sort(intervals, (x,y) => x[0] - y[0]);
        int i = 0, j = 1;
        while (j < intervals.Length) {
            var first = intervals[i];
            var second = intervals[j];
            if (first[1] >= second[0]) {
                first[1] = Math.Max(first[1], second[1]);
            }
            else {
                intervals[i+1] = intervals[j];
                i++;
            }
            j++;
        }
        return intervals[..(i+1)];;
    }
}
