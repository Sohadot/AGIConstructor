"""Run-length encoding. Task B implements `run_length_encode` to spec."""


def run_length_encode(text):
    """Run-length encode a string.

    Spec (Task B): return a list of (character, count) tuples for each maximal
    run of identical characters, in order of first appearance.
        run_length_encode("aaabbc") -> [("a", 3), ("b", 2), ("c", 1)]
        run_length_encode("x")      -> [("x", 1)]
        run_length_encode("")       -> []
    `text` is always a str. Do not add dependencies or change the signature.
    """
    raise NotImplementedError("Task B: implement run_length_encode per the spec above")
