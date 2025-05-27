import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        int[][] arr = new int[N][M];
        Queue<int[]> queue = new LinkedList<>();
        int answer = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
                if(arr[i][j] == 1) {
                    queue.add(new int[]{i, j, 0});
                }
            }
        }
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            answer = Math.max(answer, cur[2]);
            int[][] direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for(int[] d : direction) {
                int x = cur[0] + d[0];
                int y = cur[1] + d[1];
                if(x >= 0 && y >= 0 && x < N && y < M && arr[x][y] == 0) {
                    arr[x][y] = 1;
                    queue.add(new int[]{x, y, cur[2] + 1});
                }
            }
        }
        boolean canFill = true;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(arr[i][j] == 0) {
                    canFill = false;
                }
            }
        }
        if(canFill)
            System.out.println(answer);
        else
            System.out.println("-1");
    }
}