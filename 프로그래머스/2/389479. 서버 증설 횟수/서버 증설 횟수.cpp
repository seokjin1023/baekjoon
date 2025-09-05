#include <string>
#include <vector>

using namespace std;

int solution(vector<int> players, int m, int k) {
    int answer = 0;
    vector<int> server(players.size());
    for(int i = 0; i < players.size(); i++) {
        if((server[i] + 1) * m <= players[i]) {
            int add_server = players[i] / m - server[i];
            answer += add_server;
            for(int j = i; j < i + k; j++) {
                if(j > players.size())
                    break;
                server[j] += add_server;
            }
        }
    }
    return answer;
}