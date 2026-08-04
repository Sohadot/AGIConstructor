"""Basic statistics. Task A fixes a deterministic bug in `median`."""


def mean(values):
    """Arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values):
    """Median of a non-empty list of numbers.

    BUG (Task A): for an even number of values this returns the lower of the two
    middle values instead of their average. For example median([1, 2, 3, 4])
    returns 2 but should return 2.5.
    """
    if not values:
        raise ValueError("median() requires at least one value")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    # Even length: should average the two central values.
    return ordered[mid - 1]
