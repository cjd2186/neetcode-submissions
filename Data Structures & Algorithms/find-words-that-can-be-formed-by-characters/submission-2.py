#nlogn * n -> sort every array of letters

#alternative O(n^3)--> remove letter in chars from every word char by char
#after removal, another pass to get items that are empty --> get lens from words

#maybe group words into one string, so less iteration
#idea --> check if letter is in chars, if 
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = list(chars)
        goldenChars = chars.copy()
        total_good = 0
        for word in words:
            curr_good = 0
            discarded = ""
            for char in word:
                if char in chars:
                    curr_good +=1
                    chars.remove(char)
                    discarded += char
                else:
                    curr_good = 0
                    break
            chars += discarded
            discard = ""
            total_good += curr_good

        return total_good

