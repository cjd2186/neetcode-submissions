#One pass but use a list of hashmaps
#First pass
# get count frequency for each words

#Second pass
# go through indices, if count in hashmap for words are <= count of chars hashmap add to good

#Time: O(n) where n is the number of total chars in words
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        wordFreqs = [Counter(list(word)) for word in words]
        charsFreqs = Counter(list(chars))
        
        good = 0
        for i in range(len(wordFreqs)):
            word = wordFreqs[i]
            goodBool = True
            for key,val in word.items():
                if word[key] > charsFreqs[key]:
                    goodBool = False
                    break
            if goodBool:
                good += len(words[i])
        return good