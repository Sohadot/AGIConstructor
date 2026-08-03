from mathkit.stats import mean, median


def test_mean_basic():
    assert mean([2, 4, 6]) == 4


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    # Fails at the pinned fixture commit (Task A bug: returns 2, should be 2.5).
    assert median([1, 2, 3, 4]) == 2.5


def test_median_single():
    assert median([7]) == 7
