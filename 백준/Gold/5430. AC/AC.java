import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < T; i++) {
            String func = sc.nextLine();
            int arrNum = Integer.parseInt(sc.nextLine());
            Deque<Integer> arr = new ArrayDeque<>();
            String nums = sc.nextLine();
            nums = nums.replaceAll("[\\[\\]\\s]", "");
            String[] parts = nums.split(",");
            for (String part : parts) {
                if (part.isEmpty()) continue;
                arr.add(Integer.parseInt(part));
            }

            boolean isError = false;
            boolean isStart = true;

            for (char instruction : func.toCharArray()) {
                if (instruction == 'R') {
                    isStart = !isStart;
                } else if (instruction == 'D') {
                    if (arr.isEmpty()) {
                        System.out.println("error");
                        isError = true;
                        break;
                    }
                    if (isStart)
                        arr.removeFirst();
                    else
                        arr.removeLast();
                }
            }

            if (isError) continue;

            StringBuilder sb = new StringBuilder();
            sb.append("[");
            Iterator<Integer> it = isStart ? arr.iterator() : arr.descendingIterator();
            while (it.hasNext()) {
                sb.append(it.next());
                if (it.hasNext()) sb.append(",");
            }
            sb.append("]");
            System.out.println(sb.toString());
        }
    }
}
