#Algo --> hashmap, find char frequency for each word, compare freqs
#O(m), length of all words * O(n) number of words --> each character is counted once

#get frequency of each word/letter take the min
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordFreqs = Counter(words[0])
        
        for word in words:
            letterCount = Counter(word)
            for letter in wordFreqs:
                if letter in letterCount:
                    wordFreqs[letter] = min(wordFreqs[letter], letterCount[letter])
                else:
                    wordFreqs[letter] = 0
        output = []
        
        for letter, freq in wordFreqs.items():
            for i in range(freq):
                output.append(letter)
        return output