package Other;

// greedy
public class JumpGame {
    public boolean canJump(int[] A) {
        int max = 0;
        for(int i=0;i<A.length;i++){
            if(i>max) {return false;}
            max = Math.max(A[i]+i,max);
        }
        return true;
    }

    public static void main(String args[]) {
        JumpGame j = new JumpGame();
        int[] input = {1,2,2,0,0,1};
        System.out.println("Can reach last index: " + j.canJump(input));
    }
}
