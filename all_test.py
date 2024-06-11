import pytest
import random 
from all_task import create_array, lookup_num

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