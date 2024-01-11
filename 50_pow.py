# https://leetcode.com/problems/powx-n/solutions/749109/python-recursive-solution-faster-than-99/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursively
        def func(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return func(base * base, exponent // 2)
            else:
                return base * func(base * base, (exponent - 1) // 2)

        f = func()
        
        return float(f) if n >= 0 else 1/f
