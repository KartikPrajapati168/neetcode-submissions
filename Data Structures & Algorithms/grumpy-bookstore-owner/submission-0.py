class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        
        # step 1:count already satisfied customers
        total=0
        for i in range(n):
            if grumpy[i]==0:
                total+=customers[i]
        
        # step 2:calculate initial window sum
        window_sum=0
        for i in range(minutes):
            if grumpy[i]==1:
                window_sum += customers[i]
        
        max_gain = window_sum
        
        # Step 3: Apply Sliding Window
        for i in range(minutes, n):
            # Remove outgoing element
            outgoing = i - minutes

            if grumpy[outgoing] == 1:
                window_sum -= customers[outgoing]
                
            # Add incoming element
            if grumpy[i] == 1:
                window_sum += customers[i]
                
            print(window_sum)
                
            # Update maximum gain
            max_gain = max(max_gain, window_sum)
        
        # Step 4: Return final answer
        return total + max_gain