package Array;

import java.util.Arrays;

// https://leetcode.com/problems/boats-to-save-people/
//Sort people.
//        For the current heaviest person, we try to let him go with the lightest person.
//        As all people need to get on the boat.
//        If the sum of weight is over the limit, we have to let the heaviest go alone.
//        No one can take the same boat with him.
//
//        At the end of for loop, it may happen that i = j.
//        But it won't change the result so don't worry about it.
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
