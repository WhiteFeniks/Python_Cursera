import random

A = list(map(int, input().split()))


def CountSort(nums):
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
        return CountSort(s_nums) + e_nums + CountSort(m_nums)


print(*CountSort(A))
