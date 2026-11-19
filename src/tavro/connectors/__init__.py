"""Data source connectors for Deep Research."""

from tavro.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from tavro.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import tavro.connectors.obsidian  # noqa: F401

try:
    import tavro.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import tavro.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.imap  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import tavro.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import tavro.connectors.news_rss  # noqa: F401
except ImportError:
    pass
