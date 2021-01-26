# class Solution:
#     def threeSum(self, nums):
#         n = len(nums)
#         nums.sort()
#         ans = list()
#
#         # 枚举 a
#         for first in range(n):
#             # 需要和上一次枚举的数不相同
#             if first > 0 and nums[first] == nums[first - 1]:
#                 continue
#             # c 对应的指针初始指向数组的最右端
#             third = n - 1
#             target = -nums[first]
#             # 枚举 b
#             for second in range(first + 1, n):
#                 # 需要和上一次枚举的数不相同
#                 if second > first + 1 and nums[second] == nums[second - 1]:
#                     continue
#                 # 需要保证 b 的指针在 c 的指针的左侧
#                 while second < third and nums[second] + nums[third] > target:
#                     third -= 1
#                 # 如果指针重合，随着 b 后续的增加
#                 # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
#                 if second == third:
#                     break
#                 if nums[second] + nums[third] == target:
#                     ans.append([nums[first], nums[second], nums[third]])
#
#         return ans
# #
#
# class Solution:
#     def threeSumClosest(self, nums, target):
#         nums.sort()
#         n = len(nums)
#         best = 10 ** 7
#
#         # 根据差值的绝对值来更新答案
#         def update(cur):
#             nonlocal best
#             if abs(cur - target) < abs(best - target):
#                 best = cur
#
#         # 枚举 a
#         for i in range(n):
#             # 保证和上一次枚举的元素不相等
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             # 使用双指针枚举 b 和 c
#             j, k = i + 1, n - 1
#             while j < k:
#                 s = nums[i] + nums[j] + nums[k]
#                 # 如果和为 target 直接返回答案
#                 if s == target:
#                     return target
#                 update(s)
#                 if s > target:
#                     # 如果和大于 target，移动 c 对应的指针
#                     k0 = k - 1
#                     # 移动到下一个不相等的元素
#                     while j < k0 and nums[k0] == nums[k]:
#                         k0 -= 1
#                     k = k0
#                 else:
#                     # 如果和小于 target，移动 b 对应的指针
#                     j0 = j + 1
#                     # 移动到下一个不相等的元素
#                     while j0 < k and nums[j0] == nums[j]:
#                         j0 += 1
#                     j = j0
#
#         return best

class Solution:
    def threeSum(self, nums):

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

x = Solution()
print(x.threeSum([0,1,1,2,3,3]))