"""
    Determine how many ways a travel in a grid can go from the top left corner
    to the bottom right corner where the traveler's motion is limited to either
    going to the right or down.

    Given (x, y), the dimensions of the gridTraveler will return the number of
    possible moves
"""


def gridTraveler(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if (m, n) == (1, 1):
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m, n)] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[(m, n)]


for x, y in [(1, 1), (2, 3), (3, 2), (3, 3), (18, 18)]:
    print(f'gridTraveler({x}, {y}) = {gridTraveler(x, y)}')
