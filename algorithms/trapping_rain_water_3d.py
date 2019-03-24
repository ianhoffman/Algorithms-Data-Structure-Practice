import heapq


DIRECTIONS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]
        

def trap_rain_water_3d(elevations):
    """

    Given a 3-dimensional map of elevations, determine how much rainwater can be trapped.

    Note — this was super hard. I cheated a bit.

    Idea is actually not that bad, once you get the hang of it: ultimately, rainwater can only exit the elevation map via the 
    borders of the map (it can only flow "down"). Thus we begin with the lowest possible border elevation. We check its adjacent
    squares (not squares in the border!); if they are lower, we can be *assured* that no water will flow out of them. (Note: 
    it actually has only one adjacent square (or 0, if it's a corner), since all other squares are also in the border.)

    Now, if that square has a lower elevation than *any existing other square we've already looked at* (this is where the heap
    stuff comes in), we know that any water adjacent to and lower than it *also* has no way of flowing out of the elevation map.
    That's because, even if the water is able to flow "down" to another lower, adjacent square, that water will eventually need
    to flow out of the elevation map via a square which is guaranteed to be *higher in elevation* than the first square we 
    processed (thanks, heapq).

    This is how the algorithm proceeds in general: we look at the square with the lower elevation, add its neighbors to the heap,
    updates the depth, and continue.

    Input: a 3-dimensional elevation map (a list of list of integers).
    Output: the depth of that elevation map (an integer).

    """
    heap = []
    visited = {}
    result = 0

    # Process the borders first since we know everything must flow out through them.
    for i in range(len(elevations)):
        for j in range(len(elevations[i])):
            if i in (0, len(elevations) - 1) or j in (0, len(elevations[i]) - 1):
                heapq.heappush(heap, (elevations[i][j], i, j))
                visited[(i, j)] = True

    while heap:
        # Get the lowest looked-at elevation
        lowest_height, i, j = heapq.heappop(heap)
        for d in DIRECTIONS:
            # For each of its neighbors, if that neighbor is not visited and on the map...
            if 0 <= i + d[0] < len(elevations) and 0 <= j + d[1] < len(elevations[i]) and (i + d[0], j + d[1]) not in visited:
                elevation = elevations[i + d[0]][j + d[1]]
                # Set the bounding height to the maximum of the neighbor and the current lowest height
                bounding_height = max(lowest_height, elevation)
                # Add the bounding height to heap. The neighbors of this square will be processed to see if they can
                # "flow out" through the bounding height.
                heapq.heappush(heap, (bounding_height, i + d[0], j + d[1]))
                # If the elevation is greater than the current lowest height, then this does nothing.
                # Otherwise we update by the difference between.
                result += bounding_height - elevation
                # Mark this square as visited so we don't double count it.
                visited[(i + d[0], j + d[1])] = True

    return result


if __name__ == '__main__':
    height_map = [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]
    print(trap_rain_water_3d(height_map))