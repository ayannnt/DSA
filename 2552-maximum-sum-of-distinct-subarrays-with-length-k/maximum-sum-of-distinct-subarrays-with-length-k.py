from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = defaultdict(int)
        window_sum = 0
        ans = 0

        # Build the first window
        for i in range(k):
            window_sum += nums[i]
            freq[nums[i]] += 1

        if len(freq) == k:
            ans = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            left = nums[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            window_sum -= left

            right = nums[i]
            freq[right] += 1
            window_sum += right

            if len(freq) == k:
                ans = max(ans, window_sum)

        return ans