class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        n = len(nums)
        for i in range(n-2):
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                secondNum = nums[j]
                thirdNum = nums[k]
                sum = firstNum + secondNum + thirdNum
                if sum > 0:
                    k-=1
                elif sum < 0:
                    j+=1
                else:
                    triplets.add((firstNum, secondNum, thirdNum))
                    j+=1
                    while j < k and nums[j] == nums[j - 1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1

        return triplets