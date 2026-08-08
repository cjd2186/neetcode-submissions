#naive?
#track the frequency of every character in the string
#output (max(odd) - min(even)) --> want max difference
#Time: O(n) --> iterate through entirity of s
#Space: O(n) -- dict will have at most 26 spots
class Solution:
    def maxDifference(self, s: str) -> int:
        charMap = defaultdict(str)
        for char in s:
            if char not in charMap:
                charMap[char] = 0    
            charMap[char] +=1
        frequencies = list(charMap.values())
        odd_freqs = [freq for freq in frequencies if freq%2==1]
        even_freqs = [freq for freq in frequencies if freq%2==0]
        return max(odd_freqs)-min(even_freqs)
        