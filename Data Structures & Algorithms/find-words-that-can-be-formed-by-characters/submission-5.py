#One pass but use a list of hashmaps
#First pass
# get count frequency for each words

#Second pass
# go through indices, if count in hashmap for words are <= count of chars hashmap add to good

#Time: O(n) where n is the number of total chars in words
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