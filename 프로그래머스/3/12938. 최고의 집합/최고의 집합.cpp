#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer(n);
    if(s < n) {
        return { -1 };
    }
    if(s % n == 0) {
        fill(answer.begin(), answer.end(), s / n);
    }
    else {
        int down = n - (s - s / n * n);
        fill(answer.begin(), answer.begin() + down, s / n);
        fill(answer.begin() + down, answer.end(), s / n + 1);
    }
    return answer;
}