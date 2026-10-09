class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int a = 0;
        int b = 1;
        int maxProfit = 0;

        while (b < prices.size()) {
            if (prices[a] < prices[b]){
                int profit = prices[b] - prices[a];
                maxProfit = max(maxProfit, profit); 
            }else {
                a = b;
            }
            b++;
        }
        return maxProfit;
    }
};
