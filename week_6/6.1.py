import random


A = list(map(int, input().split()))
B = list(map(int, input().split()))


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def merge(A, B):
    nums = A + B
    sort = quicksort(nums)
    i = 0
    while i < len(sort):
        print(sort[i], end=" ")
        i += 1


merge(A, B)
