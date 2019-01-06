"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""


def two_sum_brute_force(nums, target):  # O(n^2)
    for i, n_1 in enumerate(nums):
        for j, n_2 in enumerate(nums[i + 1:]):
            if n_1 + n_2 == target:
                return i, j + i + 1


def two_sum_optimized_1(nums, target):  # O(nlogn)
    sorted_indices = sorted(
        range(len(nums)),
        key=lambda n: nums[n]
    )  # O(nlogn)

    high = len(sorted_indices) - 1
    low = 0

    while high != low:  # O(n)
        s = nums[sorted_indices[low]] + nums[sorted_indices[high]]
        if s == target:
            return tuple(sorted([
                sorted_indices[low],
                sorted_indices[high]
            ]))
        elif s > target:
            high -= 1
        else:
            low += 1


def two_sum_optimized_2(nums, target):  # O(n)
    num_to_idx = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in num_to_idx:
            return num_to_idx[complement], i
        num_to_idx[n] = i


if __name__ == '__main__':
    assert two_sum_brute_force(
        [1, 2, 3, 4],
        6
    ) == (1, 3)

    assert two_sum_brute_force(
        [1, 3, 4, 2],
        6
    ) == (2, 3)

    assert two_sum_optimized_1(
        [1, 2, 3, 4],
        6
    ) == (1, 3)

    assert two_sum_optimized_1(
        [1, 3, 4, 2],
        6
    ) == (2, 3)

    assert two_sum_optimized_1(
        [1, 3, 4, 2],
        7
    ) == (1, 2)

    assert two_sum_optimized_1(
        [1, 3, 4, 2],
        10
    ) is None

    assert two_sum_optimized_1(
        [1, 3, 4, 2],
        0
    ) is None

    assert two_sum_optimized_2(
        [1, 2, 3, 4],
        6
    ) == (1, 3)

    assert two_sum_optimized_2(
        [1, 3, 4, 2],
        6
    ) == (2, 3)

    assert two_sum_optimized_2(
        [1, 3, 4, 2],
        7
    ) == (1, 2)

    assert two_sum_optimized_2(
        [1, 3, 4, 2],
        10
    ) is None

    assert two_sum_optimized_2(
        [1, 3, 4, 2],
        0
    ) is None

