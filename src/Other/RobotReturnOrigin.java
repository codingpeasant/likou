package Other;

public class RobotReturnOrigin {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;

        for (char move : moves.toCharArray()) {
            switch (move) {
                case 'U': y++; break;
                case 'D': y--; break;
                case 'L': x--; break;
                case 'R': x++;
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
