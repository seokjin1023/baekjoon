import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NK = br.readLine().split(" ");
        int N = Integer.parseInt(NK[0]);
        int K = Integer.parseInt(NK[1]);
        int[][] item = new int[N][2]; //weight and value
        for (int i = 0; i < N; i++) {
            String[] itemVal = br.readLine().split(" ");
            item[i][0] = Integer.parseInt(itemVal[0]);
            item[i][1] = Integer.parseInt(itemVal[1]);
        }
        int[][] dp = new int[N][K + 1];
        for (int i = item[0][0]; i < K + 1; i++) {
            dp[0][i] = item[0][1];
        }
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < K + 1; j++) {
                if (j < item[i][0])
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - item[i][0]] + item[i][1]);
            }
        }
        System.out.println(dp[N - 1][K]);
    }
}