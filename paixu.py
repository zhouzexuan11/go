def insertion_sort(arr):
    # 遍历列表中的每个元素
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 将当前元素插入到已排序序列中的正确位置
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
