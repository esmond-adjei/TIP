from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(numRows-1): #3: 0,1,2
            next_row = [1,]
            for j in range(1, len(triangle[i])): #3: 1,2 
                next_row.append(triangle[i][j-1] + triangle[i][j]) #3: next_row = trig[0][0] + trig[0][1]
            next_row.append(1) # next_row = [1,1+]
            triangle.append(next_row)
        return triangle
    

sol = Solution()

print(sol.generate(5))