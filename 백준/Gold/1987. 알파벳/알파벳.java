import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int answer = 0;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static int R, C;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NK = br.readLine().split(" ");
        R = Integer.parseInt(NK[0]);
        C = Integer.parseInt(NK[1]);
        char[][] map = new char[R][C];
        for(int i = 0; i < R; i++) {
            String line = br.readLine();
            for(int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
            }
        }
        dfs(map, new HashSet<>(), 0, 0);
        System.out.print(answer);
    }
    private static void dfs(char[][] map, Set<Character> visited, int row, int col) {
        char alpha = map[row][col];
        if(visited.contains(alpha))
            return;
        visited.add(alpha);
        answer = Math.max(answer, visited.size());
        for(int[] direction : directions) {
            int x = row + direction[0];
            int y = col + direction[1];
            if(x >= 0 && y >= 0 && x < R && y < C)
                dfs(map, visited, x, y);
        }
        visited.remove(alpha);
    }
}