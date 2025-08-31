#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <climits>

using namespace std;

string solution(string s) {
    int min_val = INT_MAX;
    int max_val = INT_MIN;
    
    stringstream ss(s);
    int num;
    
    while(ss >> num) {
        max_val = max(max_val, num);
        min_val = min(min_val, num);
    }
    string answer = to_string(min_val) + " " + to_string(max_val);
    return answer;
}