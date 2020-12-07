"""
    Description: given a sum and a array of positive integers determine if there
    exists sums in the array that equal the given sum
"""


def canSum(target, arr):
    if target in arr or target == 0:
        return True
    if target < 0:
        return False
    for num in arr:
        remainder = target - num
        if canSum(remainder, arr):
            return True
    return False


testCases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (7, [2, 4]), (8, [2, 3, 5]), (300, [7, 14])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={canSum(targetSum, numbers)}')

