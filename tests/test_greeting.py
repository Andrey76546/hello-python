import pytest

from hello.greeting import greet, sum_range


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Python", "Hello, Python!"),
        ("CI", "Hello, CI!"),
    ],
)
def test_greet(name: str, expected: str) -> None:
    assert greet(name) == expected


def test_sum_range() -> None:
    assert sum_range(1, 10) == 55
    assert sum_range(1, 100) == 5050


def test_sum_range_single_value() -> None:
    assert sum_range(7, 7) == 7
