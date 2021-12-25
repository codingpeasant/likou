package Array;

import java.util.Arrays;

// https://leetcode.com/problems/boats-to-save-people/
public class BoatsToSavePeople {
    // Greedy is optimal here
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i, j;
        for (i = 0, j = people.length - 1; i <= j; j--) {
            if (people[i] + people[j] <= limit) {
                i++;
            }
        }
        return people.length - 1 - j;
    }

    public static void main(String[] args) {
        BoatsToSavePeople b = new BoatsToSavePeople();
        int[] input = {3,5,3,4};
        System.out.println("Min boats: " + b.numRescueBoats(input, 9));
    }
}
