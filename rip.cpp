#include <iostream>
#include <map>
#include <vector>
#include <climits>
using namespace std;

int main() {
    map<char, map<char, int>> graph = {
        {'A', {{'B', 1}, {'C', 4}}},
        {'B', {{'A', 1}, {'C', 2}, {'D', 5}}},
        {'C', {{'A', 4}, {'B', 2}, {'D', 1}}},
        {'D', {{'B', 5}, {'C', 1}}}
    };

    vector<char> nodes = {'A', 'B', 'C', 'D'};

    map<char, map<char, int>> dist;

    for (auto node : nodes) {
        for (auto n : nodes) {
            dist[node][n] = INT_MAX;
        }
        dist[node][node] = 0;

        for (auto neighbor : graph[node]) {
            dist[node][neighbor.first] = neighbor.second;
        }
    }

    cout << " RIP Simulation:\n";

    for (int step = 0; step < nodes.size() - 1; step++) {
        for (auto node : nodes) {
            for (auto neighbor : graph[node]) {
                for (auto dest : nodes) {
                    if (dist[neighbor.first][dest] != INT_MAX &&
                        dist[node][dest] > dist[neighbor.first][dest] + neighbor.second) {

                        dist[node][dest] = dist[neighbor.first][dest] + neighbor.second;
                    }
                }
            }
        }
    }

    for (auto node : nodes) {
        cout << "\nRouting table for " << node << ":\n";
        for (auto dest : nodes) {
            cout << "To " << dest << " -> cost = " << dist[node][dest] << endl;
        }
    }

    return 0;
}