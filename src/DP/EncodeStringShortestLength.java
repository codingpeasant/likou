package DP;

// https://leetcode.ca/2017-03-15-471-Encode-String-with-Shortest-Length/
public class EncodeStringShortestLength {
    public String encode(String s) {
        int length = s.length();
        String[][] dp = new String[length][length]; // min length from [i] to [j]
        for (int i = length - 1; i >= 0; i--) {
            for (int j = i; j < length; j++) {
                int curLength = j - i + 1;
                String substring = s.substring(i, j + 1);
                if (curLength <= 4)
                    dp[i][j] = substring;
                else {
                    // fromIndex = 1 is trick to find the first index of the second appearance if there is any
                    int subLength = (substring + substring).indexOf(substring, 1);
                    if (subLength < curLength) {
                        System.out.println(subLength + " " + curLength);
                        dp[i][j] = curLength / subLength + "[" + dp[i][i + subLength - 1] + "]";
                    } else {
                        dp[i][j] = substring;
                        // combine the encoded part with the suffix: 2[abbb] + c
                        for (int k = i; k < j; k++) {
                            // if encountering an encoded part at [i][k]
                            if ((dp[i][k] + dp[k + 1][j]).length() < dp[i][j].length())
                                dp[i][j] = dp[i][k] + dp[k + 1][j];
                        }
                    }
                }
            }
        }
        return dp[0][length - 1];
    }

    public static void main(String[] args) {
        EncodeStringShortestLength e = new EncodeStringShortestLength();
        System.out.println(e.encode("abbbabbbcabbbabbbc"));
    }
}
