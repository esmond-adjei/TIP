#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool first_row_has_zeros = false;
        bool first_col_has_zeros = false;

        int nr = matrix.size();
        int nc = matrix[0].size();

        for (int i = 0; i < nc; ++i) {
            if (matrix[0][i] == 0) {
                first_row_has_zeros = true;
                break;
            }
        }

        for (int i = 0; i < nr; ++i) {
            if (matrix[i][0] == 0) {
                first_col_has_zeros = true;
                break;
            }
        }

        for (int i = 1; i < nr; ++i) {
            for (int j = 1; j < nc; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for (int i = 1; i < nr; ++i) {
            for (int j = 1; j < nc; ++j) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Zero out the first row if needed
        if (first_row_has_zeros) {
            for (int i = 0; i < nc; ++i) {
                matrix[0][i] = 0;
            }
        }

        // Zero out the first column if needed
        if (first_col_has_zeros) {
            for (int i = 0; i < nr; ++i) {
                matrix[i][0] = 0;
            }
        }
    }
};
