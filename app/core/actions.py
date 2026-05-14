import json
import subprocess
from pathlib import Path
from typing import Any

from app.core.errors import ActionError, UnsafeActionError

ACTIONS_FILE = Path(__file__).resolve().parents[1] / "resources" / "actions.json"


class ActionRegistry:
    """Registry for declared safe actions only."""

    def __init__(self) -> None:
        self.actions = self._load_actions()

    def _load_actions(self) -> dict[str, dict[str, Any]]:
        if not ACTIONS_FILE.exists():
            return {}
        with ACTIONS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        actions = data.get("actions", [])
        return {action["id"]: action for action in actions if "id" in action}

    def list_actions(self) -> list[dict[str, Any]]:
        return list(self.actions.values())

    def get_action(self, action_id: str) -> dict[str, Any] | None:
        return self.actions.get(action_id)

    def run_safe_action(self, action_id: str) -> str:
        action = self.get_action(action_id)
        if action is None:
            raise ActionError(f"Unknown action: {action_id}")

        if action.get("requires_agent") or action.get("requires_authorization"):
            raise UnsafeActionError(f"Action is not allowed in pα0.2: {action_id}")

        command = action.get("command")
        if not command:
            return "Action has no executable command in this version."

        if not isinstance(command, list):
            raise UnsafeActionError("Invalid action command declaration.")

        allowed_commands = {"xdg-open"}
        if command[0] not in allowed_commands:
            raise UnsafeActionError(f"Command not allowed in pα0.2: {command[0]}")

        try:
            subprocess.Popen(command)
            return "Action started."
        except OSError as exc:
            raise ActionError(f"Could not run action {action_id}: {exc}") from exc
