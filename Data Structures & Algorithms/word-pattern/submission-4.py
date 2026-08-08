#each letter in pattern maps to one word in self
#each word in s maps to one letter in pattern

#this seems to resemble a dictionary, where the values are a set
#check set of keys and set of values
#no two letters map to the same word, no two wrds map to the same letter
#space O(n + m)
#time O(n + m)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        letter_mapping = defaultdict(str)
        word_mapping = defaultdict(str)
        if len(pattern) != len(s):
            return False

        for word, letter in zip(s, pattern):
            #check if the letter already has a letter_mapping
            if not letter_mapping[letter]:
                letter_mapping[letter] = word
            else:
                if letter_mapping[letter] != word:
                    return False
            #check if the word already has a word_mapping
            if not word_mapping[word]:
                word_mapping[word] = letter
            else:
                if word_mapping[word] != letter:
                    return False  
        return True