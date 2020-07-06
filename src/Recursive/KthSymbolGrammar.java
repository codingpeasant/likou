package Recursive;

public class KthSymbolGrammar {
    public int kthGrammar(int N, int K) {
        if (N == 1) return 0;

        if (K % 2 == 0) {
            return kthGrammar(N - 1, K / 2) == 0 ? 1 : 0; // binary tree
        } else {
            return kthGrammar(N - 1, (K + 1)/ 2) == 0 ? 0 : 1;
        }
    }

    public static void main(String[] args) {
        KthSymbolGrammar k = new KthSymbolGrammar();
        System.out.println("Value: " + k.kthGrammar(4, 6));
    }
}
