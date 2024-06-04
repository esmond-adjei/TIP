from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = {'q', 'w','e','r','t','y','u','i','o','p'}
        second_row = {'a','s','d','f','g','h','j','k','l'}
        third_row = {'z','x','c','v','b','n','m'}

        # ["Hello","Alaska","Dad","Peace"]
        # -> ["Alaska","Dad"]
        
        # 1. first_row as a set, word to set
        # 2. check if each word of list is a subset of either row
        # store words that are that prove true in a return list

        res = []
        for word in words: # O(n)
            word_set = set(word.lower()) # O(n)*2
            if word_set.issubset(first_row) or \
                word_set.issubset(second_row) or \
                word_set.issubset(third_row): # O(n)*3
                res.append(word) # O(1)
        # total: O(n) (O(n)*2 + O(n)*3) = O(n^2) * 5 (very bad)
        return res


    def findWords_2(self, words: List[str]) -> List[str]:
        # elegant but no more efficient
        rows = {
            1: set('qwertyuiop'),
            2: set('asdfghjkl'),
            3: set('zxcvbnm')
        }

        res = []
        for word in words:
            word_set = set(word.lower())
            for row, row_set in rows.items():
                if word_set.issubset(row_set):
                    res.append(word)
                    break

        return res