package Other;

// https://leetcode.com/problems/elimination-game/
public class EliminationGame {
    public int lastRemaining(int n) {
        boolean left = true;
        int remaining = n;
        int step = 1;
        int head = 1;
        while (remaining > 1) {
            if (left || remaining % 2 == 1) {
                head = head + step; // when left to right, move the head
            }
            remaining = remaining >> 1; // every iteration subtract half of the element
            step = step << 1; // every iteration doubles the gap
            left = !left;
        }
        return head;
    }

    public static void main(String[] args) {
        EliminationGame e = new EliminationGame();
        System.out.println(e.lastRemaining(9));
    }
}
