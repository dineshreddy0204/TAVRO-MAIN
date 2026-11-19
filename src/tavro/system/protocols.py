"""Structural protocols for substituting fakes in place of TavroSystem."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Protocol

if TYPE_CHECKING:
    from tavro.core.config import TavroConfig
    from tavro.core.events import EventBus
    from tavro.engine._stubs import InferenceEngine
    from tavro.security.capabilities import CapabilityPolicy
    from tavro.sessions.session import SessionStore
    from tavro.tools._stubs import BaseTool
    from tavro.tools.storage._stubs import MemoryBackend
    from tavro.traces.collector import TraceCollector
    from tavro.traces.store import TraceStore


class OrchestratorDeps(Protocol):
    """Minimum surface of TavroSystem that QueryOrchestrator depends on.

    Tests can satisfy this with a lightweight class — no need to construct
    the full TavroSystem dataclass or materialize every subsystem.
    """

    config: TavroConfig
    bus: EventBus
    engine: InferenceEngine
    engine_key: str
    model: str
    agent_name: str
    tools: List[BaseTool]
    memory_backend: Optional[MemoryBackend]
    capability_policy: Optional[CapabilityPolicy]
    rate_limiter: Optional[Any]
    session_store: Optional[SessionStore]
    trace_store: Optional[TraceStore]
    trace_collector: Optional[TraceCollector]  # written by _run_agent

    # Optional attribute (getattr with default) — declared for type clarity.
    _skill_few_shot_examples: Any
