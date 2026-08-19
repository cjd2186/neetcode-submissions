#Idea is that you find the track first occurance of each letter and find next occurence each time
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        res = -1
        for i, letter in enumerate(s):
            if letter in char_index:
                res = max(res, i -  char_index[letter] - 1)
            else:
                char_index[letter] = i
        return res
