#Algo, sort, then remove dupes and have counter, if counter not in arr, add to output
#remove dupes instead of set to ensure to extra space, remove operation is O(n) too

#sort --> O(n log n) --> can use a dictionary instead?
#for O(n) and no extra space would have to just go through the list once

#one pass --> make output have indexes as values
#second pass --> replace discovered indexes with 0
#third pass --> return list without 0s
#3*O(n) --> O(n) time --> but uses extra space

#no extra space --> modify nums in place
#make nums[abs(num)] negative
#index of remaining positive nums are omitted from array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] = -nums[abs(num)-1]
        print(nums)
                
        #build output
        return [i+1 for i, num in enumerate(nums) if num>0]