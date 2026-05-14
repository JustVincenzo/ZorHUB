import json
import shutil
from pathlib import Path
from typing import Any

from app.core.config import ConfigManager

COMPONENTS_FILE = Path(__file__).resolve().parents[1] / "resources" / "components.json"


class ComponentService:
    def __init__(self, config: ConfigManager) -> None:
        self.config = config
        self.components = self._load_components()

    def _load_components(self) -> list[dict[str, Any]]:
        if not COMPONENTS_FILE.exists():
            return []
        with COMPONENTS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("components", [])

    def list_components(self) -> list[dict[str, Any]]:
        result = []
        for component in self.components:
            item = component.copy()
            item["status"] = self.detect_status(component)
            item["enabled"] = self.config.is_component_enabled(
                component["id"], bool(component.get("default_enabled", True))
            )
            result.append(item)
        return result

    def detect_status(self, component: dict[str, Any]) -> str:
        if not component.get("implemented", False):
            return "not_implemented"
        detect = component.get("detect", {})
        binary = detect.get("binary")
        if binary:
            return "available" if shutil.which(binary) else "missing"
        return "unknown"
