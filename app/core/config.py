import json
from typing import Any

from app.core.paths import CONFIG_FILE, ensure_app_dirs
from app.core.errors import ConfigError

DEFAULT_CONFIG: dict[str, Any] = {
    "appearance": "system",
    "user_mode": "simple",
    "first_run": True,
    "logs_enabled": True,
    "background_allowed": False,
    "enabled_components": {},
}

VALID_APPEARANCE_MODES = {"system", "light", "dark"}
VALID_USER_MODES = {"simple", "advanced"}


class ConfigManager:
    def __init__(self) -> None:
        ensure_app_dirs()
        self.config: dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> dict[str, Any]:
        if not CONFIG_FILE.exists():
            self.save()
            return self.config

        try:
            with CONFIG_FILE.open("r", encoding="utf-8") as file:
                loaded = json.load(file)

            if not isinstance(loaded, dict):
                raise ConfigError("Configuration file does not contain a valid JSON object.")

            self.config = DEFAULT_CONFIG.copy()
            self.config.update(loaded)
            self._validate()
            return self.config

        except json.JSONDecodeError as exc:
            raise ConfigError(f"Invalid JSON configuration: {exc}") from exc
        except OSError as exc:
            raise ConfigError(f"Could not read configuration file: {exc}") from exc

    def save(self) -> None:
        try:
            ensure_app_dirs()
            with CONFIG_FILE.open("w", encoding="utf-8") as file:
                json.dump(self.config, file, indent=2, ensure_ascii=False)
        except OSError as exc:
            raise ConfigError(f"Could not save configuration file: {exc}") from exc

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value
        self._validate()
        self.save()

    def set_component_enabled(self, component_id: str, enabled: bool) -> None:
        enabled_components = self.config.setdefault("enabled_components", {})
        if not isinstance(enabled_components, dict):
            enabled_components = {}
            self.config["enabled_components"] = enabled_components
        enabled_components[component_id] = enabled
        self.save()

    def is_component_enabled(self, component_id: str, default: bool = True) -> bool:
        enabled_components = self.config.get("enabled_components", {})
        if not isinstance(enabled_components, dict):
            return default
        return bool(enabled_components.get(component_id, default))

    def _validate(self) -> None:
        if self.config.get("appearance") not in VALID_APPEARANCE_MODES:
            self.config["appearance"] = DEFAULT_CONFIG["appearance"]

        if self.config.get("user_mode") not in VALID_USER_MODES:
            self.config["user_mode"] = DEFAULT_CONFIG["user_mode"]

        self.config["first_run"] = bool(self.config.get("first_run", True))
        self.config["logs_enabled"] = bool(self.config.get("logs_enabled", True))
        self.config["background_allowed"] = bool(self.config.get("background_allowed", False))

        if not isinstance(self.config.get("enabled_components"), dict):
            self.config["enabled_components"] = {}
