class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        int n = s.length();
        vector<int> distances(n);

        // First pass: Left to Right
        int prev = -n;
        for (int i = 0; i < n; ++i) {
            if (s[i] == c) {
                prev = i;
            }
            distances[i] = i - prev;
        }

        // Second pass: Right to Left
        for (int i = prev - 1; i >= 0; --i) {
            if (s[i] == c) {
                prev = i;
            }
            distances[i] = min(distances[i], prev - i);
        }

        return distances;
    }
};
