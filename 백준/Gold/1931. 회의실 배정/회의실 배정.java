import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][2];
        for(int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }
        Arrays.sort(arr, (a, b) -> {
            if(a[0] == b[0]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });
        int answer = 0;
        int endTime = -1;
        for(int[] time : arr) {
            int start = time[0];
            int end = time[1];
            if(endTime == -1) {
                endTime = end;
                continue;
            }
            if(start >= endTime) {
                answer++;
                endTime = end;
            }
            else {
                if (end < endTime)
                    endTime = end;
            }
        }
        answer++;
        System.out.println(answer);
    }
}
