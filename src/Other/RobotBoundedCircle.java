package Other;

// https://leetcode.com/problems/robot-bounded-in-circle/
// after one sequence of instructions,
//        if chopper return to the origin, he is obvious in a circle.
//        if chopper finishes with face not towards north,
//        it will get back to the initial status in another one or three sequences.
public class RobotBoundedCircle {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0, dir = 0; // 0: north(up), 1: right, 2: down, 3: left
        int d[][] = {{0, 1}, {1, 0}, {0, -1}, { -1, 0}};
        for (int j = 0; j < instructions.length(); ++j)
            if (instructions.charAt(j) == 'R')
                dir = (dir + 1) % 4;
            else if (instructions.charAt(j) == 'L')
                dir = (dir + 3) % 4;
            else {
                x += d[dir][0]; y += d[dir][1];
            }
        return x == 0 && y == 0 || dir > 0;
    }

    public static void main(String[] args) {
        RobotBoundedCircle r = new RobotBoundedCircle();
        String ins = "GL";
        System.out.println(r.isRobotBounded(ins));
    }
}
