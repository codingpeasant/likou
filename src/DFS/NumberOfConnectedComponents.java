package DFS;

public class NumberOfConnectedComponents {
    boolean[] visited;
    private void connectedComponents(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            if (!visited[i]) {
                DFS(matrix, i);
            }
        }
    }

    private void DFS(int[][] matrix, int i) {
        visited[i] = true;
        System.out.print(i + " ");
        for (int j = 0; j < matrix.length; j++) {
            if (matrix[i][j] == 1 && !visited[j]) {
                DFS(matrix, j);
            }
        }
        System.out.print("\n");
    }

    // Driver method
    public static void main(String[] args) {
        int M[][] = new int[][]{
                {0, 1, 0, 0, 0},
                {1, 0, 0, 0, 0},
                {0, 0, 0, 1, 0},
                {0, 0, 1, 0, 1},
                {0, 0, 0, 1, 0},
        };
        NumberOfConnectedComponents N = new NumberOfConnectedComponents();
        N.visited = new boolean[M.length];
        System.out.println("Connected components are: ");
        N.connectedComponents(M);
    }
}
