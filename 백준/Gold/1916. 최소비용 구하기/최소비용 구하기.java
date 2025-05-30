import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        Map<Integer, List<int[]>> bus = new HashMap<>();
        for(int i = 0; i < m; i++) {
            String[] inform =  br.readLine().split(" ");
            bus.computeIfAbsent(Integer.parseInt(inform[0]), k -> new ArrayList<>())
                    .add(new int[]{Integer.parseInt(inform[1]), Integer.parseInt(inform[2])});
        }
        String[] SE =  br.readLine().split(" ");
        int start =  Integer.parseInt(SE[0]);
        int end = Integer.parseInt(SE[1]);
        int[] minPrice = new int[n + 1];
        Arrays.fill(minPrice, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.add(new int[]{start, 0});
        while(!pq.isEmpty()) {
            int[] cur = pq.poll();

            if(cur[0] == end) {
                break;
            }
            for(int[] edge : bus.getOrDefault(cur[0],  new ArrayList<>())) {
                if(minPrice[edge[0]] > edge[1] + cur[1]) {
                    pq.add(new int[]{edge[0], edge[1] + cur[1]});
                    minPrice[edge[0]] = edge[1] + cur[1];
                }
            }
        }
        System.out.println(minPrice[end]);
    }
}
