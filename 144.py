a=[1,5,1,1,6,4]
1,6,7,8,14,18
a.sort()

print(a)

def wiggleSort(nums):
    import random

    n = len(nums)

    # Helper: find kth largest using QuickSelect
    def findKthLargest(k):
        def quickselect(left, right, k_smallest):
            pivot = nums[random.randint(left, right)]
            # Dutch partition
            i, j, k = left, left, right
            while j <= k:
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] < pivot:
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
                else:
                    j += 1
            if k_smallest < i:
                return quickselect(left, i - 1, k_smallest)
            elif k_smallest > k:
                return quickselect(k + 1, right, k_smallest)
            else:
                return nums[k_smallest]
        return quickselect(0, len(nums) - 1, k)

    # Step 1: Find median
    median = findKthLargest((n - 1) // 2)

    # Step 2: Virtual indexing trick
    def mapped_index(i):
        return (1 + 2 * i) % (n | 1)

    # Step 3: Three-way partition around median using virtual indexing
    left, i, right = 0, 0, n - 1
    while i <= right:
        mi = mapped_index(i)
        if nums[mi] > median:
            nums[mapped_index(left)], nums[mi] = nums[mi], nums[mapped_index(left)]
            left += 1
            i += 1
        elif nums[mi] < median:
            nums[mi], nums[mapped_index(right)] = nums[mapped_index(right)], nums[mi]
            right -= 1
        else:
            i += 1