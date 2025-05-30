import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int n = Integer.parseInt(NM[0]);
        int m = Integer.parseInt(NM[1]);
        Map<Integer, List<int[]>> connect = new HashMap<>();
        List<int[]> connections = new ArrayList<>();
        for(int i = 0; i < m; i++) {
            String[] inform =  br.readLine().split(" ");
            connections.add(new int[] {Integer.parseInt(inform[0]), Integer.parseInt(inform[1]),
            Integer.parseInt(inform[2])});
        }
        connections.sort((a, b) -> a[2] - b[2]);
        parent = new int[n + 1];
        for(int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }
        int answer = 0;
        for(int[] connection : connections) {
            if(canUnion(connection[0], connection[1])) {
                answer += connection[2];
                union(connection[0], connection[1]);
            }
        }
        System.out.println(answer);
    }

    private static int find(int x) {
        if(parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    private static boolean canUnion(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        return rootA != rootB;
    }

    private static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        parent[rootA] = rootB;
    }
}
