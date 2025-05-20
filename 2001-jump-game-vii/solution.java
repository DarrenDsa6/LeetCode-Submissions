import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length();
        if (s.charAt(n - 1) != '0') return false; 
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0); 
        int farthest = 0; 

        while (!queue.isEmpty()) {
            int currentIndex = queue.poll();
            for (int jump = Math.max(currentIndex + minJump, farthest + 1); jump <= Math.min(currentIndex + maxJump, n - 1); jump++) {
                if (s.charAt(jump) == '0') {
                    if (jump == n - 1) return true; 
                    queue.offer(jump);
                }
            }

            farthest = Math.max(farthest, currentIndex + maxJump); // Update farthest reached index
        }

        return false;
    }
}

