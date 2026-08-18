class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_string = "".join(words)
        char_count = Counter(char_string)
        needed_count = len(words)
        for count in char_count.values():
            if count % needed_count != 0:
                return False
        return True

        
# aaabc, abc, bc, bc
#remove common chars from all words
#if number of leftover chars = #words true, otw false
#need count of each char to be equal to #words