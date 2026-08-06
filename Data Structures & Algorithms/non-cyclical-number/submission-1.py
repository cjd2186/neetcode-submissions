class Solution:
    def isHappy(self, n: int) -> bool:
        traversed = set()
        while True:
            digits = [int(digit) for digit in list(str(n))]
            print(digits)
            combo = 0
            for digit in digits:
                combo += digit **2
            if combo == 1:
                return True
            else:
                if combo in traversed:
                    return False
                n = combo
                traversed.add(combo)