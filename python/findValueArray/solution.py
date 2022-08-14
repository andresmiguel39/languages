from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and target == 1:
            result = [0,0]
        else:
            result = [-1,-1]
        idx = findSearchPoint(nums, target)
        print("idx: ", idx)
        if idx == -1:
            return result
        count_right = idx
        for i in range(idx,0,-1):
            if count_right == 0 or nums[count_right-1] < target:
                result[0] = count_right
                break
            count_right = count_right - 1
        count_left = idx
        for i in range(idx, len(nums)):
            if count_left == len(nums)-1 or nums[count_left+1] > target :
                result[1] = count_left
                break
            count_left = count_left + 1
        return result
                
def findSearchPoint(nums: List[int], target: int) -> int:
    idx, left, right = -1, 0, len(nums)-1
    for i in range(left, right):
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return idx

def searchRangeLoop(self, nums: List[int], target: int) -> List[int]:
        count = -1
        result = [-1,-1]
        for i in nums:
            count = count + 1
            if target == i and result[0] == -1:
                result[0] = count
            if target == i:
                result[1] = count
        return result
                
def searchPoint(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        print(left, right)
        return 