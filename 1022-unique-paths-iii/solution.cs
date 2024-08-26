public class Solution {
    int[] dx=new int[4]{1,-1,0, 0};
    int[] dy=new int[4]{0, 0,1,-1};    
    int output=0;
    public int UniquePathsIII(int[][] grid) {
        int emptyplace=0;
        int[] begin=new int[2];
        int[] end=new int[2];
        for(int i=0;i<grid.Length;i++){
            for(int j=0;j<grid[0].Length;j++){
                if (grid[i][j]==0) emptyplace++;
                if (grid[i][j]==1) begin=new int[2]{i,j};
                if (grid[i][j]==2) end=new int[2]{i,j};
            }
        }
        for(int n=0;n<4;n++){
            backtrack(begin[0]+dx[n],begin[1]+dy[n],grid, end,emptyplace);
        }
        return output;
    }
    public void backtrack(int i, int j, int[][] grid,int[] end, int emptyplace){
        if (i<0||i>=grid.Length) return;
        if (j<0||j>=grid[0].Length) return;
        if (i==end[0] && j==end[1]){
            output+= emptyplace==0 ? 1  : 0 ;
            return;
        }
        if (grid[i][j]!=0) return;
        for( int m =0;m<4;m++){
            emptyplace--;
            grid[i][j]=-2;
            backtrack(i+dx[m],j+dy[m],grid,end,emptyplace);
            grid[i][j]=0;
            emptyplace++;
        }
        return;
    }
}
