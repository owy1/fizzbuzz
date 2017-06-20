import pytest


FIZZBUZZ_TABLE = [
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (16, "16"),
    (20, "Buzz"),
    (21, "Fizz"),
    (25, "Buzz")
]


@pytest.mark.parametrize("num_in, out", FIZZBUZZ_TABLE)
def test_fizzbuzz(num_in, out):
    """Testing the fizzbuzz function."""
    from fizzbuzz import fizzbuzz
    assert fizzbuzz(num_in) == out
