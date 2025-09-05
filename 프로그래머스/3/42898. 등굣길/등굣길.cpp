#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    vector<vector<int>> path(m, vector<int>(n));
    for(int i = 0; i < puddles.size(); i++) 
        path[puddles[i][0] - 1][puddles[i][1] - 1] = -1;
    
    for(int i = 0; i < n; i++) {
        if(path[0][i] == -1)
            break;
        path[0][i] = 1;
    }
    for(int i = 1; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(path[i][j] == -1)
                continue;
            if(j == 0) {
                if(path[i - 1][j] == -1)
                    path[i][j] = 0;
                else
                    path[i][j] = path[i - 1][j];
            }
            else {
                if(path[i - 1][j] != -1 && path[i][j - 1] != -1)
                    path[i][j] = path[i - 1][j] + path[i][j - 1];
                else if(path[i - 1][j] != -1)
                    path[i][j] = path[i - 1][j];
                else if(path[i][j - 1] != -1)
                    path[i][j] = path[i][j - 1];
                else
                    path[i][j] = 0;
            }
            path[i][j] %= 1000000007;
        }
    }
    return path[m - 1][n - 1];
}