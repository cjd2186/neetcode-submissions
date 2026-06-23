class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x=0
        y=len(s) -1
        while x<y:
            z = s[x] 
            s[x] = s[y]
            s[y] = z
            x+=1
            y-=1