class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        if (numRows == 0)
            return triangle;
        triangle.push_back({1});
        
        for (int i = 1; i < numRows; ++i) {
            vector<int> nextRow = {1};
            for (int j = 1; j < triangle[i-1].size(); ++j) {
                nextRow.push_back(triangle[i-1][j-1] + triangle[i-1][j]);
            }
            nextRow.push_back(1);
            triangle.push_back(nextRow);
        }
        return triangle;
    }
};