import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();
        int startV = sc.nextInt() - 1;
        int[] shortestPath = new int[v];
        Arrays.fill(shortestPath, Integer.MAX_VALUE);
        Map<Integer, List<List<Integer>>> graph = new HashMap<>();
        for(int i = 0; i < e; i++) {
            int start = sc.nextInt() - 1;
            List<List<Integer>> list = graph.computeIfAbsent(start, k -> new ArrayList<>());
            int end = sc.nextInt() - 1;
            int weight = sc.nextInt();
            list.add(Arrays.asList(end, weight));
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{startV, 0});
        while(!pq.isEmpty()) {
            int[] current = pq.poll();

            if(shortestPath[current[0]] <= current[1])
                continue;
            shortestPath[current[0]] = current[1];
            List<List<Integer>> list = graph.getOrDefault(current[0], new ArrayList<>());
            for(List<Integer> edge : list) {
                if(shortestPath[edge.get(0)] > current[1] + edge.get(1))
                    pq.offer(new int[]{edge.get(0), current[1] + edge.get(1)});
            }
        }
        for(int i = 0; i < v; i++) {
            if(shortestPath[i] == Integer.MAX_VALUE)
                System.out.println("INF");
            else
                System.out.println(shortestPath[i]);
        }
    }
}
