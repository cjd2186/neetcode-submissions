#get counts using counter and sort array
#counter puts most most frequency at the beginning but doenst do the desc order
#if tie, sort nums in decreasing order
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        #make sublist when freqs are the same and just sort that sublist in desc?
        #reverse the second item to make it invert the sort!
        freqs = sorted(freqs.items(), key=lambda item: (item[1], -item[0]))
        output = []
        for (num, freq) in freqs:
            for i in range(freq):
                output.append(num)
        
        return output