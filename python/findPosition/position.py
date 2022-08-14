from typing import List

class Position:
    def searchPosition(self, nums: List[int], target: int) -> int:
        idx = findMiddle(nums, target)
        print("idx: ", idx)
        if nums[idx] == target:
            return idx
        if nums[idx] < target:
            for i in range(idx, target):
                if nums[i] > target or i == len(nums)-1:
                    return i
        if nums[idx] > target:
            for i in range(len(nums),idx,-1):
                if nums[i] < target or i == 0:
                    return i + 1
        return idx
                
def findMiddle(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    for i in range(left, right):
        mid = int((left + right) / 2)
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
        return target
    return left
