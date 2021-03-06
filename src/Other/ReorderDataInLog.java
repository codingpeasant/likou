package Other;

import java.util.Arrays;
import java.util.Comparator;

public class ReorderDataInLog {
    public String[] reorderLogFiles(String[] logs) {

        Comparator<String> myComp = (s1, s2) -> {
            int s1SpaceIndex = s1.indexOf(' ');
            int s2SpaceIndex = s2.indexOf(' ');
            char s1FirstCharacter = s1.charAt(s1SpaceIndex+1);
            char s2FirstCharacter = s2.charAt(s2SpaceIndex+1);

            if (s1FirstCharacter <= '9') {
                if (s2FirstCharacter <= '9') return 0;
                else return 1;
            }
            if (s2FirstCharacter <= '9') return -1;

            int preCompute = s1.substring(s1SpaceIndex+1).compareTo(s2.substring(s2SpaceIndex+1));
            if (preCompute == 0) return s1.substring(0,s1SpaceIndex).compareTo(s2.substring(0,s2SpaceIndex));
            return preCompute;
        };

        Arrays.sort(logs, myComp);
        return logs;
    }

    public static void main(String[] args) {
        ReorderDataInLog r = new ReorderDataInLog();
        String[] input = {"dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"};
        System.out.println(Arrays.toString(r.reorderLogFiles(input)));
    }
}
