class Solution {
private:
    bool numIsEven(int num) {
        int count_digit = 1;
        while (num) {
            num /=10;
            count_digit++ ;
        }
        return count_digit % 2;
    }
public:
    int findNumbers(vector<int>& nums) {
        int cnt = 0;
        for (int n : nums) {
            if (numIsEven(n))
                cnt++;
        }
        return cnt;
    }
};