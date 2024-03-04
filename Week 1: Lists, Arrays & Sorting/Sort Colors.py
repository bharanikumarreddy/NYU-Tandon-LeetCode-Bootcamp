class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low=0
        mid=0
        high=len(nums)-1
        while mid <=high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low +=1
                mid +=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[high]= nums[high],nums[mid]
                high-=1
        return nums
        """
  The Dutch National Flag algorithm efficient and appropriate approach.

Here's a brief explanation of the Dutch National Flag algorithm :

1. Initialize three pointers: `low`, `mid`, and `high`. `low` will point to the start of the array, `mid` will iterate through the array, and `high` will point to the end of the array.
2. Iterate through the array using the `mid` pointer.
3. If `nums[mid]` is 0, swap `nums[mid]` with `nums[low]`, increment both `mid` and `low`.
4. If `nums[mid]` is 1, no action is needed. Simply increment `mid`.
5. If `nums[mid]` is 2, swap `nums[mid]` with `nums[high]`, decrement `high`.
6. Continue this process until `mid` is greater than `high`.

This algorithm efficiently sorts the array in-place with a time complexity of O(n), where n is the number of elements in the array.
        """
        