class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #O(n)
        countText = Counter(text)
        countBalloon = Counter("balloon")
        balloons = len(text)
        for count in countBalloon:
            balloons = min(balloons, countText[count] // countBalloon[count])
        return balloons