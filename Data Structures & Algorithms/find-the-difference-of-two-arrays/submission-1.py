#O(n^2) naive is to check if each item in nums1 in nums2 then switch

#track frequency of both simultaneously
# if key is 1, its only in nums1, 2, only in nums2, 0 means both/neither

#len(nums1) != len(nums2) --> just append rest as part of nums1
#have counter store the count of each item
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        
        for num in nums1:
            if counter[num] == 1:
                continue
            counter[num]+=1
        for num in nums2:
            if counter[num] == 2:
                continue
            counter[num]+=2
                    
        output1 = []
        output2 = []

        for i, num in counter.items():
            if num == 1:
                output1.append(i)
            elif num == 2:
                output2.append(i)

        return [output1, output2]
        