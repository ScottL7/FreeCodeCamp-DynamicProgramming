"""
    Description: given a sum and a array of positive integers determine if there
    exists sums in the array that equal the given sum
"""


def howSum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        result = howSum(remainder, arr, memo)
        if result is not None:
            result.append(num)
            memo[target] = result
            return memo[target]
    memo[target] = None
    return None


"""
    m = target sum
    n = length of array
    
    Brute Force 
    time: O(n^m * m)
    space: O(m)
    
    Memoize Version
    time: O(n*m*m) or O(n * m^2)
    space: O(m*m) or O(m^2)
"""

testCases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (7, [2, 4]), (8, [2, 3, 5]), (300, [7, 14])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={howSum(targetSum, numbers)}')

