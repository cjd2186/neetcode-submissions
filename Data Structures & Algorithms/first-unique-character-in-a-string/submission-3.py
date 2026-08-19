#optimized hashmap, just store first occurence of each letter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = defaultdict(int)
        for i, letter in enumerate(s):
            if letter not in uniques:
                uniques[letter] = i
            else:
                uniques[letter] = len(s)
        res = min(uniques.values())
        return -1 if res == len(s) else res