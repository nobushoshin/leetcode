class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        answers = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res = 'FizzBuzz'
            elif i % 3 == 0:
                res = 'Fizz'
            elif i % 5 == 0:
                res = 'Buzz'
            else:
                res = str(i)
            answers.append(res)

        return answers

n = 5
solution = Solution()
res = solution.fizzBuzz(n)
print(res)