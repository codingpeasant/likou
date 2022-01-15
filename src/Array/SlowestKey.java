package Array;

public class SlowestKey {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int n = releaseTimes.length;
        int maxDifference = releaseTimes[0];
        char bestChar = keysPressed.charAt(0);
        for (int i = 1; i < n; i++) {
            int difference = releaseTimes[i] - releaseTimes[i-1];

            if (difference > maxDifference || (difference == maxDifference && keysPressed.charAt(i) > bestChar)) {
                maxDifference = difference;
                bestChar = keysPressed.charAt(i);
            }
        }
        return bestChar;
    }

    public static void main(String[] args) {
        SlowestKey s = new SlowestKey();
        int[] releaseTime = {9,29,49,50};
        String keyPressed = "cbcd";
        System.out.println(s.slowestKey(releaseTime, keyPressed));
    }
}
