import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);
        int[][] map = new int[N][M];
        for(int i = 0; i < N; i++) {
            String line = br.readLine();
            for(int j = 0; j < M; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }
        int answer = Integer.MAX_VALUE;
        //벽한번 꺠기전 = 0 / 깬 후 1
        boolean[][][] visited = new boolean[N][M][2];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1, 1}); //row, col, canBreak, distance
        visited[0][0][0] = true;
        visited[0][0][1] = true;
        int[][] distances = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            if(cur[0] == N - 1 && cur[1] == M - 1) {
                answer = Math.min(answer, cur[3]);
                continue;
            }
            for(int[] distance : distances) {
                int x = cur[0] + distance[0];
                int y = cur[1] + distance[1];
                if(x >= 0 && x < N && y >= 0 && y < M) {
                    if(map[x][y] == 1) {
                        if(cur[2] == 1) {
                            if(!visited[x][y][1]) {
                                visited[x][y][1] = true;
                                q.add(new int[]{x, y, 0, cur[3] + 1});
                            }
                        }
                    }
                    else {
                        if(cur[2] == 1 && !visited[x][y][0]) {
                            visited[x][y][0] = true;
                            q.add(new int[]{x, y, cur[2], cur[3] + 1});
                        }
                        else if(cur[2] == 0 && !visited[x][y][1]) {
                            visited[x][y][1] = true;
                            q.add(new int[]{x, y, cur[2], cur[3] + 1});
                        }

                    }
                }
            }
        }
        if(answer == Integer.MAX_VALUE)
            System.out.println("-1");
        else
            System.out.println(answer);
    }
}
