# cant just sort, need to preserve the position of each num
#may need an O(n^2) -- check num with all proceeding nums

#use hashmap, but for what?
#every time you see a number already, an extra pair can be made with previous pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        good = 0
        for num in nums:
            seen[num] = 0
        
        for num in nums:
            good+= seen[num]
            seen[num] += 1
        return good
'''
1 2; 
1 3; 
1 1;
1 1; 
1 3;
2 3;
2 1;
2 1;
2 3;
3 1;
3 1;
3 3;
1 1;
1 3;
1 3;
'''