#Algo
#check if each letter in abbr is followed by N chars before next letter

#go through abbr, increment i by the number of the abbr, checking letters in word with each i
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            char = abbr[j]
            print(char, "!")
            #if letter, check that abbr letter is correct
            if ord(char) >= 65:
                if word[i] != char:
                    return False
                i +=1
                j +=1
            #if num, increment the word pointer num times
            else:
                num = ""
                print(char, j, "erer")
                while ord(char) < 65: 
                    num += char
                    j+=1
                    if j < len(abbr):
                        char=abbr[j]
                    else:
                        break
                    
                print(num, "NUM")
                #cant have leading 0 in pointer
                if num[0] == '0':
                    return False
                i += int(num)
                if i > len(word):
                    print(i, "C")
                    return False
            print(i, j)
        print(i,j)
        return i == len(word) and j == len(abbr)