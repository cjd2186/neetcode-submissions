#O(n + m) --> two pointers

#sort both arrays
#iterate until you see they have common elements
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1, n2 = 0, 0
        output = set()
        #idea is to sort both arrays 
        #compare item at each arrays
        #if one item is geater than the other, you must increment the lesser idex
        #if the items 
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                output.add(nums1[n1])
                n1+=1
                n2+=1
            elif nums1[n1] > nums2[n2]:
                n2+=1
            elif nums2[n2] > nums1[n1]:
                n1+=1
        return list(output)