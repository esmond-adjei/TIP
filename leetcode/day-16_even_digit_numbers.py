from types import List

class Solution:
    """
    Theory is simple:
    1. Count the number of digits in a number
    2. Check if the number of digits is even
    3. Do this for each number in the list
    4. Return the count of numbers that have even digits
    """
    @staticmethod
    def even_digits(num):
        count_digits = 1
        while k:=num // 10:
            num = k
            count_digits += 1
        return count_digits % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        # main problem would be determining even digits
        count_even = 0
        for num in nums:
            if self.even_digits(num):
                count_even += 1
        return count_even
# solution works. Let's optimize it


if __name__ == '__main__':
    my_solution = Solution()
    print(my_solution.findNumbers([12,345,2,6,7896])) # 2
