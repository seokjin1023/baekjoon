import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        boolean[] visited = new boolean[100_001];

        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[]{N, 0});
        visited[N] = true;

        while (!dq.isEmpty()) {
            int[] cur = dq.poll();
            int pos = cur[0];
            int time = cur[1];

            if (pos == K) {
                System.out.println(time);
                return;
            }

            int next = pos * 2;
            if (next <= 100_000 && !visited[next]) {
                visited[next] = true;
                dq.addFirst(new int[]{next, time});
            }

            // 1초 이동: x - 1
            if (pos - 1 >= 0 && !visited[pos - 1]) {
                visited[pos - 1] = true;
                dq.addLast(new int[]{pos - 1, time + 1});
            }

            // 1초 이동: x + 1
            if (pos + 1 <= 100_000 && !visited[pos + 1]) {
                visited[pos + 1] = true;
                dq.addLast(new int[]{pos + 1, time + 1});
            }
        }
    }
}
