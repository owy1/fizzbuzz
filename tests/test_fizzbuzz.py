import pytest


FIZZBUZZ_TABLE = [
    (0, "0"),
    (1, "1"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz")
]


@pytest.mark.parametrize("num_in, out", FIZZBUZZ_TABLE)
def test_fizzbuzz(num_in, out):
    """Testing the fizzbuzz function."""
    from fizzbuzz import fizzbuzz
    assert fizzbuzz(num_in) == out
