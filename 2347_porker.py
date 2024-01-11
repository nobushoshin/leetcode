class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        
        cards = {}
        for rank in ranks:
            if not rank in cards:
                cards[rank] = 1
            else:
                cards[rank] += 1
        if max(cards.values()) >= 3:
            return "Three of a Kind"
        elif max(cards.values()) == 2:
            return "Pair"
        else:
            return "High Card"

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]
solution = Solution()
res = solution.bestHand(ranks, suits)
print(res)