class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
      
        number_of_bills = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            number_of_bills[bill] += 1
            change = bill - 5
            if change == 0:
                continue
            # Return change in the order of the largest denomination
            for key in reversed(number_of_bills):
                if key > change:
                    continue                
                quotient = change // key
                for i in range(quotient, 0, -1):
                    if i <= number_of_bills[key]:
                        change -= key * i
                        number_of_bills[key] -= i
                        break
                if change == 0:
                    break
                  
            if change > 0:
                return False

        return True
