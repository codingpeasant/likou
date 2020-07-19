package Other;

// Great example about when you cannot use for loop easily / set elements in array as empty easily
public class StringCompression {
    public int compress(char[] chars) {
        int indexAns = 0, index = 0;
        while(index < chars.length){
            char currentChar = chars[index];
            int count = 0;
            while(index < chars.length && chars[index] == currentChar){
                index++;
                count++;
            }
            chars[indexAns++] = currentChar;
            if(count != 1)
                for(char c : Integer.toString(count).toCharArray())
                    chars[indexAns++] = c;
        }
        return indexAns;
    }

    public static void main(String[] args) {
        StringCompression s = new StringCompression();
        String input = "aabbbbbbb";
        System.out.println("Compressed length: " + s.compress(input.toCharArray()));
    }
}
