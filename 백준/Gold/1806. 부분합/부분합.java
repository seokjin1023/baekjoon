import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NS = br.readLine().split(" ");
        int N = Integer.parseInt(NS[0]);
        int S = Integer.parseInt(NS[1]);
        if(S == 0) {
            System.out.println(1);
            return;
        }
        int[] arr = new int[N];
        String[] nums = br.readLine().split(" ");
        for(int i = 0; i < N; i++)
            arr[i] = Integer.parseInt(nums[i]);

        int answer = Integer.MAX_VALUE;
        int left = 0, right = -1;
        int sum = 0;
        while(true) {
            if(sum >= S) {
                while(sum - arr[left] >= S) {
                    sum -= arr[left++];
                }
            }
            if(sum >= S)
                answer = Math.min(answer, right - left + 1);
            if(right == N - 1) break;
            sum += arr[++right];
        }
        if(answer == Integer.MAX_VALUE)
            System.out.println(0);
        else
            System.out.println(answer);
    }
}
