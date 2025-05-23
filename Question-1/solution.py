from typing import List

"""
Question:

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be 
planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an 
integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
rule and false otherwise.


Explanation:

- Stop the process of checking the positions for planting the flowers as soon as count becomes equal to n. 
- If count never becomes equal to n, n flowers cannot be planted at the empty positions.


Complexities:

- Time complexity: O(n). A single scan of the flowerbed array of size n is done.
- Space complexity: O(1). Constant extra space is used.
"""


############### Solution #################
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) -
                                   1) or (flowerbed[i + 1] == 0)

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


############### Test Cases #################
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # returns True
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # returns False

    # Added test cases
    print(solution.canPlaceFlowers([0, 0, 0, 0, 0], 2))  # returns True
    print(solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))  # returns False
    print(solution.canPlaceFlowers([0], 1))  # returns True
    print(solution.canPlaceFlowers([1], 0))  # returns True
    print(solution.canPlaceFlowers([1], 1))  # returns False
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 2))  # returns True


################# Run code #################
"""
In the terminal run command:

python solution.py
"""
