package DP;

// F(i, n) = G(i-1) * G(n-i)	1 <= i <= n
// G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
public class UniqueBinarySearchTrees {
    public int numTrees(int n) {
        int [] G = new int[n+1];
        G[0] = G[1] = 1;

        for(int i=2; i<=n; ++i) {
            for(int j=1; j<=i; ++j) {
                G[i] += G[j-1] * G[i-j];
            }
        }
        return G[n];
    }

    public static void main(String args[]) {
        UniqueBinarySearchTrees u = new UniqueBinarySearchTrees();
        System.out.println("unique: " + u.numTrees(4));
    }
}
