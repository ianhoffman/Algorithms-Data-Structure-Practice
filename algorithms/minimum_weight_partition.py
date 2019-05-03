def minimum_weight_partition(A, k):
    cache = {}

    def helper(i, j, n):
        if (i, j, n) in cache:
            return cache[(i, j, n)]

        if n == 0 or j <= 0:
            s = sum(A[:i])
        else:
            s = min(
                # Opt to use 1 less partition;
                helper(i, j, n - 1),
                # Place the kth partition at j.
                # Now we compare the partition from j...i against
                # the largest partition ending before j.
                max(sum(A[j:i]), helper(j, j - 1, n - 1)),
                # Alternatively, we add the jth element to this partition and recurse.
                helper(i, j - 1, n)
            )

        cache[(i, j, n)] = s
        return s

    return helper(len(A), len(A) - 1, k)


if __name__ == '__main__':
    print(minimum_weight_partition([1], 0))
    print(minimum_weight_partition([1, 1], 1))
    print(minimum_weight_partition([1, 1], 2))
    print(minimum_weight_partition([1, 1], 10))
    print(minimum_weight_partition([1, 2], 1))
    print(minimum_weight_partition([1, 2, 1], 1))
    print(minimum_weight_partition([1, 2, 1], 2))
    print(minimum_weight_partition([1, 2, 1, 1], 1))
    print(minimum_weight_partition([1, 2, 1, 1], 2))
    print(minimum_weight_partition([1, 2, 1, 1, 2], 2))
    print(minimum_weight_partition([1, 2, 1, 1, 2], 3))

