from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        distances = [0] * n

        prev = -n
        for i in range(n):
            if s[i] == c:
                prev = i
            distances[i] = i - prev

        for i in range(prev - 1, -1, -1):
            if s[i] == c:
                prev = i
            distances[i] = min(distances[i], prev - i)

        return distances
