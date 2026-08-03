from mathkit.encode import run_length_encode


def test_encode_basic():
    assert run_length_encode("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]


def test_encode_single():
    assert run_length_encode("x") == [("x", 1)]


def test_encode_empty():
    assert run_length_encode("") == []


def test_encode_no_runs():
    assert run_length_encode("abc") == [("a", 1), ("b", 1), ("c", 1)]
