class Solution {

    public int MaxProfit (int [] prices) {

        int toBuy = prices[0];

        int bestProfit = 0;

        for ( int i = 1; i < prices.Length; i++ ) {
            if ( prices[i] < toBuy) {
                toBuy = prices[i];
            } else if  (bestProfit < prices[i]- toBuy){ 
                bestProfit = prices[i]-toBuy;
            }
        }

        return bestProfit;
    }
}