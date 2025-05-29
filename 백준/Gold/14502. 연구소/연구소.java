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
        List<int[]> virus = new ArrayList<>();
        List<int[]> blank = new ArrayList<>();
        List<List<int[]>> combination = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            for(int j = 0; j < M; j++) {
                int value = Integer.parseInt(line[j]);
                map[i][j] = value;
                if(value == 0)
                    blank.add(new int[]{i, j});
                if(value == 2)
                    virus.add(new int[]{i, j});
            }
        }
        combine(blank, 3, 0, new ArrayList<>(), combination);

        int maxSafe = 0;

        for(List<int[]> list : combination) {
            int[][] temp = deepCopy(map);
            for(int[] wallPos: list) {
                temp[wallPos[0]][wallPos[1]] = 1;
            }
            maxSafe = Math.max(maxSafe, countSafe(temp, virus));
        }
        System.out.println(maxSafe);
    }

    private static int countSafe(int[][] map, List<int[]> virus) {
        int safe = 0;
        Queue<int[]> queue = new LinkedList<>(virus);
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            for(int[] direction : directions) {
                int x = cur[0] + direction[0];
                int y = cur[1] + direction[1];
                if(x < 0 || x >= map.length || y < 0 || y >= map[0].length) continue;
                if(map[x][y] == 0) {
                    map[x][y] = 2;
                    queue.add(new int[]{x, y});
                }
            }
        }

        for(int i = 0; i < map.length; i++) {
            for(int j = 0; j < map[i].length; j++) {
                if(map[i][j] == 0) {
                    safe++;
                }
            }
        }
        return safe;
    }
    public static int[][] deepCopy(int[][] original) {
        if (original == null) return null;

        int[][] copy = new int[original.length][];
        for (int i = 0; i < original.length; i++) {
            copy[i] = original[i].clone();  // 각 행을 복사
        }
        return copy;
    }
    // 조합 구하는 함수
    private static void combine(List<int[]> arr, int r, int start, List<int[]> current, List<List<int[]>> result) {
        if (current.size() == r) {
            List<int[]> copy = new ArrayList<>();
            for (int[] item : current) {
                copy.add(item.clone());  // 배열 복사
            }
            result.add(copy);
            return;
        }

        for (int i = start; i < arr.size(); i++) {
            current.add(arr.get(i));
            combine(arr, r, i + 1, current, result); // 다음 인덱스부터 재귀
            current.remove(current.size() - 1); // 백트래킹
        }
    }
}
