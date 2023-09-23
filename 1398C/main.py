# https://codeforces.com/problemset/problem/1398/C

import sys
from collections import defaultdict

test_cases = []


def parse_input():
    num_cases = int(sys.stdin.readline())

    for i in range(num_cases):
        array_length = int(sys.stdin.readline())
        array = [-1] * array_length
        for i, n in enumerate(sys.stdin.readline()[:-1]):
            array[i] = int(n)

        test_cases.append(array)


def good_subarrays(arr) -> int:
    answer = 0
    sum = 0
    map = defaultdict(int)
    map[0] = 1

    for i, num in enumerate(arr):
        sum += num
        answer += map[sum - i - 1]
        map[sum - i - 1] += 1

    return answer


# # print(good_subarrays([1, 2, 0]))
# print(good_subarrays([2, 0, 0, 2, 1, 0, 2, 2, 0, 0, 1, 2, 0, 2, 1, 1, 2, 1, 0]))
parse_input()

for test_case in test_cases:
    print(good_subarrays(test_case))

# [3, 6, 1, 71]
