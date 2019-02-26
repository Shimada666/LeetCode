class NumArray:
    def __init__(self, nums):
        self.nums = [0]
        for i in nums:
            self.nums.append(i + self.nums[-1])  # 列表每次加前面一个数 dp的想法是把之前的计算结果存储到这个self.nums数组里

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]
