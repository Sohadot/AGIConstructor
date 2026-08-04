"""mathkit — tiny deterministic fixture package for REAL-LEDGER-001."""

from .stats import mean, median
from .encode import run_length_encode

__all__ = ["mean", "median", "run_length_encode"]
