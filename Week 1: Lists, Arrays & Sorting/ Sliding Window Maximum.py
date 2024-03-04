class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize the result list
        res = []

        for i in range(len(nums) - k + 1):
            # Find the maximum value in the current window and append to res
            max_val = max(nums[i:i+k])
            res.append(max_val)

        return res

        # Time Complexity: O(n*k), where n is the number of elements in the array and k is the window size.
        # Space Complexity: O(n), where n is the number of elements in the array, accounting for the space needed to store the result for each window.