import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] status = new int[N][N];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                status[i][j] = sc.nextInt();
            }
        }
        //끝과 방향을 통해 구현
        /*
        좌표의 위치는 항상 파이프의 끝을 의미함. (0, 1)
        가로 2개면 0
        세로 2개면 1
        대각선이면 2로 파이프의 방향을 나타냄.
         */
        int[][][] dp = new int[N][N][3];

        // 초기 상태: (0, 1)에 가로 방향으로 파이프가 있음
        dp[0][1][0] = 1;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(status[i][j] == 1) continue;

                // 가로
                if(j - 1 >= 0) {
                    dp[i][j][0] += dp[i][j - 1][0];
                    dp[i][j][0] += dp[i][j - 1][2];
                }

                // 세로
                if(i - 1 >= 0) {
                    dp[i][j][1] += dp[i - 1][j][1];
                    dp[i][j][1] += dp[i - 1][j][2];
                }

                // 대각선
                if(i - 1 >= 0 && j - 1 >= 0) {
                    if(status[i - 1][j] == 0 && status[i][j - 1] == 0) {
                        dp[i][j][2] += dp[i - 1][j - 1][0];
                        dp[i][j][2] += dp[i - 1][j - 1][1];
                        dp[i][j][2] += dp[i - 1][j - 1][2];
                    }
                }
            }
        }

        int answer = dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2];
        System.out.println(answer);
    }
}
