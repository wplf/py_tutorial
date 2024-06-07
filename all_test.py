import pytest
from day_1 import create_array


@pytest.mark.parametrize("param1", [i for i in range(10)])
def test_create_array(param1):
    result = create_array(param1)
    assert len(result) == 10, "数组长度应该是 10"
    for index, value in enumerate(result):
        assert index * param1  ==  value, f"索引 {index} 的值应该是 {index}，但实际是 {value}"