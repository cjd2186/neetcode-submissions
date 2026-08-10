#Simple --> use hashset, return min of hashset values
#challenge is o and l have two letters

#sorting is O(nlogn) --> want to do it in O(n) time instead
#need twice as many o and l as min number of other letters
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = {}
        for letter in "balloon":
            balloons[letter] = 0
        
        for letter in text:
            if letter in "balloon":
                balloons[letter]+=1
        min_letter = min(balloons.values())
        if balloons["o"] == min_letter or balloons["l"] == min_letter:
            return min_letter//2
        if balloons["o"] >= 2*min_letter and balloons["l"] >= 2*min_letter:
            return min_letter
        return min(balloons["o"]//2, balloons["l"]//2)