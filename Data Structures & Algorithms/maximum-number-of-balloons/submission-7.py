#Simple --> use hashset, return min of hashset values
#challenge is o and l have two letters

#sorting is O(nlogn) --> want to do it in O(n) time instead
#need twice as many o and l as min number of other letters
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = defaultdict(int)
        
        for letter in text:
            if letter in "balon":
                balloons[letter]+=1
        if len(balloons) < 5:
            return 0     
        balloons["l"] //=2
        balloons["o"] //=2
        return min(balloons.values())