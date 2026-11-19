"""Learning primitive -- router policies, reward functions, learning."""

from __future__ import annotations

from tavro.learning._stubs import (
    QueryAnalyzer,
    RewardFunction,
    RouterPolicy,
    RoutingContext,
)
from tavro.learning.agents.agent_evolver import AgentConfigEvolver
from tavro.learning.learning_orchestrator import LearningOrchestrator
from tavro.learning.optimize.llm_optimizer import LLMOptimizer
from tavro.learning.optimize.optimizer import OptimizationEngine
from tavro.learning.optimize.store import OptimizationStore
from tavro.learning.routing.complexity import (
    ComplexityQueryAnalyzer,
    score_complexity,
)
from tavro.learning.routing.heuristic_reward import HeuristicRewardFunction
from tavro.learning.routing.router import (
    HeuristicRouter,
    build_routing_context,
)
from tavro.learning.training.data import TrainingDataMiner
from tavro.learning.training.lora import HAS_TORCH, LoRATrainer, LoRATrainingConfig


def ensure_registered() -> None:
    """Ensure all learning policies are registered in RouterPolicyRegistry."""
    from tavro.learning.routing.heuristic_policy import (
        ensure_registered as _reg_heuristic,
    )

    _reg_heuristic()

    from tavro.learning.routing.learned_router import (
        ensure_registered as _reg_learned,
    )

    _reg_learned()

    # Intelligence training (optional deps)
    try:
        import tavro.learning.intelligence  # noqa: F401
    except ImportError:
        pass

    # Orchestrator-specific training (optional deps)
    try:
        import tavro.learning.intelligence.orchestrator  # noqa: F401
    except ImportError:
        pass

    # Agent optimizers (optional deps)
    try:
        import tavro.learning.agents.dspy_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import tavro.learning.agents.gepa_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import tavro.learning.agents.ace_optimizer  # noqa: F401
    except ImportError:
        pass


__all__ = [
    "AgentConfigEvolver",
    "ComplexityQueryAnalyzer",
    "HAS_TORCH",
    "HeuristicRewardFunction",
    "HeuristicRouter",
    "LLMOptimizer",
    "LearningOrchestrator",
    "LoRATrainer",
    "LoRATrainingConfig",
    "OptimizationEngine",
    "OptimizationStore",
    "QueryAnalyzer",
    "RewardFunction",
    "RouterPolicy",
    "RoutingContext",
    "TrainingDataMiner",
    "build_routing_context",
    "ensure_registered",
    "score_complexity",
]
