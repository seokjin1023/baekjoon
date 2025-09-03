#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    for(int i = 1; i < triangle.size(); i++) {
        triangle[i][0] += triangle[i - 1][0];
        for(int j = 1; j < triangle[i].size() - 1; j++)
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j]);
        triangle[i].back() += triangle[i - 1].back();
    }
    int answer = *max_element(triangle.back().begin(), triangle.back().end());
    return answer;
}