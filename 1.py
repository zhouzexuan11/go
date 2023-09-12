python
Copy
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# 示例输入列表
numbers = [5, 2, 9, 1, 3]

print("排序前：", numbers)
bubble_sort(numbers)
print("排序后：", numbers)
