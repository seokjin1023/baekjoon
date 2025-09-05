#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    priority_queue<int> pq(works.begin(), works.end());
    while(n--) {
        if(pq.empty())
            break;
        int rest_work = pq.top() - 1;
        if (rest_work > 0)
            pq.push(rest_work);
        pq.pop();
    }
    while(!pq.empty()) {
        long long num = pq.top();
        answer += (long long)num * num;
        pq.pop();
    }
    return answer;
}