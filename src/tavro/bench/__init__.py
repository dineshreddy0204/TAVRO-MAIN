"""Benchmarking framework for Tavro inference engines."""

from __future__ import annotations

from tavro.bench._stubs import BaseBenchmark, BenchmarkResult, BenchmarkSuite
from tavro.core.registry import BenchmarkRegistry


def ensure_registered() -> None:
    """Ensure all benchmark implementations are registered."""
    from tavro.bench.energy import ensure_registered as _reg_energy
    from tavro.bench.latency import ensure_registered as _reg_latency
    from tavro.bench.throughput import ensure_registered as _reg_throughput

    _reg_latency()
    _reg_throughput()
    _reg_energy()


# Trigger registration on import
ensure_registered()

__all__ = [
    "BaseBenchmark",
    "BenchmarkRegistry",
    "BenchmarkResult",
    "BenchmarkSuite",
    "ensure_registered",
]
