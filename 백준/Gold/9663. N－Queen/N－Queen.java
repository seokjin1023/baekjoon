import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] position;
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        position = new int[N];
        dfs(0);
        System.out.println(answer);
    }
    private static boolean canPut(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (position[i] == col || Math.abs(row - i) == Math.abs(col - position[i])) {
                return false;
            }
        }
        return true;
    }
    private static void dfs(int row) {
        if(row == N) {
            answer++;
            return;
        }
        for(int i = 0; i < N; i++) {
            if(canPut(row, i)) {
                position[row] = i;
                dfs(row + 1);
            }
        }
    }
}