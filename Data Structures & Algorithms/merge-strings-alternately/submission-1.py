#algo go left right left right until left/right no longer and just tack on rest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = -1
        min1 = False
        if len(word1)>len(word2):
            minLen = len(word2)
            min1 = False
        else:
            minLen = len(word1)
            min1 = True

        output = ""
        i = 0
        while i < minLen:
            print(output)
            print(i, minLen)
            output+=(word1[i])
            output+=(word2[i])
            i+=1

        if min1:
            output+= word2[i:]
        else:
            output+= word1[i:]
        return output