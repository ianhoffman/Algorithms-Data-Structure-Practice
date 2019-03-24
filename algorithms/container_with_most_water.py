def get_increasing_indices(heights):
    increasing_indices = []
    last_height = None
    for i, height in enumerate(heights):
        if last_height is None or height > last_height:
            last_height = height
            increasing_indices.append(i)
    return increasing_indices


def maxArea(heights):
    i, j = 0, len(heights) - 1
    area = 0

    increasing_indices = get_increasing_indices(heights)
    decreasing_indices = get_increasing_indices(heights[::-1])

    for i in increasing_indices:
        for j in decreasing_indices:
            j = len(heights) - j - 1
            if i >= j:
                break
            else:
                area = max(
                    min(heights[i], heights[j]) * (j - i),
                    area
                )

    return area


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    degenerate_input = list(range(15000))
    print(maxArea(degenerate_input))