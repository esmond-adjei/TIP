#include <unordered_map>


class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        unordered_map<char, int> rowMap;
        vector<string> rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};

        // Populate rowMap
        for (int i = 0; i < rows.size(); ++i) {
            for (char c : rows[i]) {
                rowMap[c] = i;
                rowMap[toupper(c)] = i;
        }

        vector<string> res;
        for (const string& word : words) {
            if (word.empty()) continue;
            int row = rowMap[word[0]];
            bool sameRow = true;
            for (char c : word) {
                if (rowMap[c] != row) {
                    sameRow = false;
                    break;
                }
            }
            if (sameRow) res.push_back(word);
        }

        return res;
    }
};
