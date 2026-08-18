#Algo

#Two patterns , 01 10
class Solution:
    def minOperations(self, s: str) -> int:
        pattern0=0
        for i in range(len(s)):
            if i%2==0 and s[i] != '0':
                pattern0 +=1
            elif i%2==1 and s[i] != '1':
                pattern0 +=1 
        
        pattern1=0
        for i in range(len(s)):
            if i%2==0 and s[i] != '1':
                pattern1 +=1
            elif i%2==1 and s[i] != '0':
                pattern1 +=1

        return min(pattern0, pattern1)