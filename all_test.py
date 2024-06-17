import random

import pytest
from all_task import *


@pytest.mark.parametrize("param1", [i for i in range(10)])
def test_create_array(param1):
    assert create_array(param1) == [x * param1 for x in range(10)]


@pytest.mark.parametrize( 
    "nums, target", [
        ([i for i in range(100)], random.randint(0, 99)) for _ in range(10)
    ]
)
def test_lookup_num(nums, target):
    assert lookup_num(nums, target) == [i for i, x in enumerate(nums) if x == target]


@pytest.mark.parametrize( 
    "nums, target, ans", [
        ([2,7,11,15], 9, [0, 1]),
        ([3,2,4], 6, [1, 2]),
        ([3,3], 6, [0, 1]),
    ]
)
def test_two_sum(nums, target, ans):
    assert two_sum(nums, target) == ans
    # S = dict()
    # for i, x in enumerate(nums):
    #     print(S, x, i)
    #     if target - x in S:
    #         return [S[target - x], i]
    #     S[x] = i


def test_plot_from_excel():
    filename = "./dataset/grade.xlsx"
    plot_from_excel(filename=filename)
    # plt.plot(df["ID"], df["Grade"])
    # plt.title("Grades by ID")
    # plt.xlabel("ID")
    # plt.ylabel("Grade")


@pytest.mark.parametrize( 
    "num, ans", [ 
        (x, x % 2 == 0) for x in range(10)
    ]
)
def test_check_even(num, ans):
    assert check_even(num) == ans
    