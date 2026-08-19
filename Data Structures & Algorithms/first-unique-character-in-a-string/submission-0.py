#Algo
#find count of each letter, search for unique chars: 26*O(n) --> O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = defaultdict(int)
        for i, letter in enumerate(s):
            if uniques[letter] == None:
                uniques[letter] = 1
            else:
                uniques[letter] += 1
        
        for i, letter in enumerate(s):
            if uniques[letter] == 1:
                return i
        return -1