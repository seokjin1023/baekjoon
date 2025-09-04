#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <queue>
#include <functional>
#include <vector>

using namespace std;

string add_clean(string time) {
    int hour = stoi(time.substr(0,2));
    int min = stoi(time.substr(3,2));
    
    min += 10;
    if (min >= 60) {
        hour += 1;
        min -= 60;
    }
    
    stringstream ss;
    ss << setfill('0') << setw(2) << hour;
    ss << ":";
    ss << setfill('0') << setw(2) << min;
    return ss.str();
}

int solution(vector<vector<string>> book_time) {
    int answer = 0;
    priority_queue<string, vector<string>, greater<string>> minHeap;
    sort(book_time.begin(), book_time.end());
    for(int i = 0; i < book_time.size(); i++)
        book_time[i][1] = add_clean(book_time[i][1]);
    for(int i = 0; i < book_time.size(); i++) {
        minHeap.push(book_time[i][1]);
        while(!minHeap.empty() && book_time[i][0] >= minHeap.top()) {
            minHeap.pop();
        }
        answer = max(answer, (int)minHeap.size());
    }
    return answer;
}