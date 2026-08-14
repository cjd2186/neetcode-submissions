#Time: O(w) --> w total number of chars in all words
#Space: O(1) --> unqiueChars is at most length 26
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        output = 0
        for word in words:
            uniqueChars = list(Counter(word).keys())
            good = True
            for char in uniqueChars:
                if char not in allowed:
                    good = False
                    break
            if good:
                output +=1
        return output