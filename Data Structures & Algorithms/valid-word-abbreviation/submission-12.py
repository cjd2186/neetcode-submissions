#Algo
#check if each letter in abbr is followed by N chars before next letter

#go through abbr, increment i by the number of the abbr, checking letters in word with each i
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            char = abbr[j]
            #if letter, check that abbr letter is correct
            if ord(char) >= 65:
                if word[i] != char:
                    return False
                i +=1
                j +=1
            #if num, increment the word pointer num times
            else:
                num = ""
                while ord(char) < 65: 
                    num += char
                    j+=1
                    if j < len(abbr):
                        char=abbr[j]
                    else:
                        break
                    
                #cant have leading 0 in pointer
                if num[0] == '0':
                    return False
                i += int(num)
                if i > len(word):
                    return False
        #if i or j are longer then the what theyre tracking, invalid
        return i == len(word) and j == len(abbr)