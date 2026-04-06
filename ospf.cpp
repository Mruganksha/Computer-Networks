#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

typedef pair<int, char> p; 

int main() {
    map<char, map<char, int>> graph = {
        {'A', {{'B', 1}, {'C', 4}}},
        {'B', {{'A', 1}, {'C', 2}, {'D', 5}}},
        {'C', {{'A', 4}, {'B', 2}, {'D', 1}}},
        {'D', {{'B', 5}, {'C', 1}}}
    };

    cout << "\nOSPF Simulation :\n";

    for (auto startPair : graph) {
        char start = startPair.first;

        map<char, int> dist;
        for (auto node : graph) {
            dist[node.first] = INT_MAX;
        }

        dist[start] = 0;

        priority_queue<p, vector<p>, greater<p>> pq;
        pq.push({0, start});

        while (!pq.empty()) {
            auto current = pq.top();
            pq.pop();

            int d = current.first;
            char node = current.second;

            for (auto neighbor : graph[node]) {
                int newDist = d + neighbor.second;

                if (newDist < dist[neighbor.first]) {
                    dist[neighbor.first] = newDist;
                    pq.push({newDist, neighbor.first});
                }
            }
        }

        cout << "\nShortest paths from " << start << ":\n";
        for (auto d : dist) {
            cout << start << " -> " << d.first << " = " << d.second << endl;
        }
    }

    return 0;
}