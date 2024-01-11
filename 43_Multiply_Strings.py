class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = self.str_to_int(num1)
        num2_int = self.str_to_int(num2)
        return str(num1_int * num2_int)

    def str_to_int(self, string):
        num = 0
        for i in range(len(string)):
            num += int(string[len(string) - 1 - i]) * (10 ** i)
        return num        

num1 = '123'
num2 = '456'
solution = Solution()
print(solution.multiply(num1, num2))