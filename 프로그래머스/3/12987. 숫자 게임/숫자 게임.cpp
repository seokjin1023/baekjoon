#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    sort(A.rbegin(), A.rend());
    sort(B.rbegin(), B.rend());
    int win = 0;
    for(int i = 0; i < A.size(); i++) {
        if(B[win] > A[i]) {
            answer += 1;
            win += 1;
        }
        else
            B.pop_back();
    }
    return answer;
}