import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int n = Integer.parseInt(NM[0]);
        int m = Integer.parseInt(NM[1]);
        arr = new int[n + 1];
        for(int i = 0; i < n + 1; i++)
            arr[i] = i;


        for(int i = 0; i < m; i++) {
            String[] instruction =  br.readLine().split(" ");
            int plus = Integer.parseInt(instruction[0]);
            int a =  Integer.parseInt(instruction[1]);
            int b =  Integer.parseInt(instruction[2]);

            if(plus == 0) {
                union(a, b);
            }
            else {
                if(find(a) == find(b))
                    System.out.println("YES");
                else
                    System.out.println("NO");
            }
        }
    }
    private static int find(int x) {
        if(arr[x] != x)
            arr[x] = find(arr[x]);
        return arr[x];
    }

    private static void union (int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if(rootA != rootB)
            arr[rootA] = rootB;
    }
}
