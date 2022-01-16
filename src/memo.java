import java.util.*;

public class ScratchPad {
    public static void main(String[] args) {
        // List to array
        List<Integer> ans1 = new ArrayList<>(); ans1.add(1);
        int[] ansArray1 = ans1.stream().mapToInt(el -> el).toArray();

        // List to 2-dimension array; Arrays.
        List<int[]> ans2 = new ArrayList<>(); ans2.add(new int[]{1, 2});
        int[][] ansArray2 = new int[ans2.size()][]; ans2.toArray(ansArray2);
        Arrays.fill(ansArray2, new int[]{3,4}); Arrays.sort(ansArray2, (a,b) -> b[0] - a[0]);

        // TreeMap floor/ceiling
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        treeMap.put(1, 1); treeMap.put(3, 1);
        treeMap.floorEntry(2); // (1,1)
        treeMap.ceilingEntry(2); // (3,1)

        // charArray to string; String to integer/integer to string
        char[] charArray = {'a', 'b', 'c'}; String s = new String(charArray);
        String ss = String.valueOf(123); int ssInt = Integer.parseInt("1234");

        // ASCII
        int[] cha = new int[10]; cha['a'] = 10; // a == 97; A == 65; 0 == 48
        System.out.println(cha[97]); // a

        // ArrayList operations; map to list
        List<Integer> ans3 = new ArrayList<>(); ans3.add(1); ans3.add(1); ans3.add(2);
        ans3.add(1, 1); ans3.remove(2); ans3.set(0, 100);
        List.of(1,2,3); ans3.addAll(Map.of("a", 1).values());

    }
}
