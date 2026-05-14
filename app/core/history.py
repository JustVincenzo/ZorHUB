import json
from datetime import datetime, timezone
from typing import Any

from app.core.paths import HISTORY_FILE, ensure_app_dirs


class HistoryManager:
    """Append-only local history for safe pα0.x events."""

    def add_event(self, event_type: str, message: str, details: dict[str, Any] | None = None) -> None:
        ensure_app_dirs()
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "type": event_type,
            "message": message,
            "details": details or {},
        }
        with HISTORY_FILE.open("a", encoding="utf-8") as file:
            file.write(json.dumps(event, ensure_ascii=False) + "\n")

    def read_events(self, limit: int = 100) -> list[dict[str, Any]]:
        if not HISTORY_FILE.exists():
            return []
        events: list[dict[str, Any]] = []
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return events[-limit:]

    def clear(self) -> None:
        ensure_app_dirs()
        HISTORY_FILE.write_text("", encoding="utf-8")
