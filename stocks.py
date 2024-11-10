class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        left_window_index = 0
        right_window_index = 1
        buyWindow = 0
        sellWindow = 0
        flag = 0

        #find intial window positions
        while right_window_index < len(prices) and prices[right_window_index] - prices[left_window_index] <= 0:
            left_window_index += 1
            right_window_index += 1

        if right_window_index == len(prices):
            return 0 
        
        buyWindow = left_window_index
        sellWindow = right_window_index

        max_profit = prices[sellWindow] - prices[buyWindow]


        while left_window_index < len(prices) - 2 and right_window_index < len(prices) - 1:
            #move right window
            while(flag == 0 and right_window_index != len(prices) - 1):
                right_window_index += 1
                profit = prices[right_window_index] - prices[buyWindow]
                if (profit > max_profit):
                    buyWindow = left_window_index
                    sellWindow = right_window_index
                    max_profit = prices[sellWindow] - prices[buyWindow]
                    flag = 1
                    temp = left_window_index +1
            while(temp <  right_window_index - 1):
                if prices[temp] < prices[buyWindow]:
                    buyWindow = left_window_index = temp
                    max_profit = prices[sellWindow] - prices[buyWindow]
                temp += 1
            flag = 0

        return max_profit    




def main():
    
    a = Solution

    print(a.maxProfit(a, [1,4,2]))


main()