class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #2**n subsets
        #decision tree
        #choose to add a number or not add a number each time
        output = []

        subset = []
        def dfs(i):
            #hit basecase, i is out of bounds --> at leaf node
            #i says which element we are currently visiting
            if i >= len(nums):
                output.append(subset.copy())
                return
            
            #decision to include nums[i]
            #left branch of decision tree
            subset.append(nums[i])
            dfs(i+1)

            #decision not to include nums[i]
            #function calls are different subsets
            subset.pop()
            #empty subset given to it
            dfs(i+1)
        dfs(0)
        return output