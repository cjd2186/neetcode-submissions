class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ""
        for num in digits:
            x+=str(num)
        y = int(x)
        y += 1
        z = list(str(y))
        return z
