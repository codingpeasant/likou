package JavaTest;

public class Test {
    public static void main(String[] args) throws Exception {
        for (int i = 0; i < 10; i++) {
            try {
                System.out.println(i);
                if (i == 5) {
                    throw new Exception("AAA");
                }
            } catch (Exception e) {

            }

        }
    }
}
