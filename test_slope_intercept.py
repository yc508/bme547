import pytest

@pytest.mark.parametrize("tuple1, tuple2, input, expected", [
    [(1,4), (2,6), 5, 12]
])



def test_linearequation(tuple1, tuple2, input, expected):
    from slope_intercept import linearequation
    answer = linearequation(tuple1, tuple2, input)
    assert answer == int(expected)

