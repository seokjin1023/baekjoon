#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>

using namespace std;

bool is_one_different(string a, string b) {
    int count = 0;
    for(int i = 0; i < a.length(); i++) {
        if(a[i] != b[i])
            count++;
    }
    if(count == 1)
        return true;
    return false;
}

int solution(string begin, string target, vector<string> words) {
    queue<pair<string, int>> count;
    vector<int> path(words.size());
    count.push({begin, 0});
    while(!count.empty()) {
        pair<string, int> word = count.front();
        count.pop();
        for(int i = 0; i < words.size(); i++) {
            if(path[i] != 0)
                continue;
            if(is_one_different(word.first, words[i])) {
                if(words[i] == target)
                    return word.second + 1;
                count.push({words[i], word.second + 1});
                path[i] = word.second + 1;
            }
        }
    }
    return 0;
}