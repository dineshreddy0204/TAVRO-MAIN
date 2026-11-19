"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from tavro.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import tavro.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.weather  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.fx_macro  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.docker_shell_exec  # noqa: F401
    import tavro.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import tavro.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.digest_collect  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.scan_chunks  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.knowledge_sql  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.knowledge_search  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.browser  # noqa: F401
    import tavro.tools.browser_axtree  # noqa: F401
except ImportError:
    pass

try:
    import tavro.tools.proactive_tools  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
