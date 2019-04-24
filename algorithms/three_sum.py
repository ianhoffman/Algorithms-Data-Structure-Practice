def three_sum(nums):
    """Generate all tuples of three numbers in the input array which sum to 0.

    The numbers must be at distinct indices in the array. Duplicate tuples are not allowed.

    :param nums: an array of integers
    :type nums: List[int]
    :return: a list of tuples satisfying sum(t) == 0
    :rtype: List[Tuple[int, int, int]]
    """
    nums.sort()
    solutions = []
    for i, num in enumerate(nums[:-1]):
        target = 0 - num
        low, high = i + 1, len(nums) - 1
        while low < high:
            s = nums[low] + nums[high]
            if s == target:
                solutions.append((num, nums[low], nums[high]))
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif s < target:
                low += 1
            else:
                high -= 1
    return solutions


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0, 0, 0, 0]))
    print(three_sum([-1, 0, 1, 0]))

