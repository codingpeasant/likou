package Other;

// https://leetcode.com/problems/robot-return-to-origin/
public class RobotReturnOrigin {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;

        for (char move : moves.toCharArray()) {
            switch (move) {
                case 'U' -> y++;
                case 'D' -> y--;
                case 'L' -> x--;
                case 'R' -> x++;
            }
        }
        return x == 0 && y == 0;
    }

    public static void main(String[] args) {
        RobotReturnOrigin r = new RobotReturnOrigin();
        String input = "UDRLLLRRR";
        System.out.println("Returned to origin: " + r.judgeCircle(input));
    }
}
