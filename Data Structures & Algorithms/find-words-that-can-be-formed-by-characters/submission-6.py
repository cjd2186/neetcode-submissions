#One pass but use a hashmap
#First pass
# get count frequency for word

#Second pass
# go through chars, if count in hashmap for words are <= count of chars hashmap add to good

#Time: O(c + w) c length of chars, w chars in words
#Space: O(1) at most 26 different chars
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsFreqs = Counter(chars)
        
        good = 0
        for word in words:
            wordFreq = Counter(word)
            goodBool = True
            for char in wordFreq:
                if wordFreq[char] > charsFreqs[char]:
                    goodBool = False
                    break
            if goodBool:
                good += len(word)
        return good