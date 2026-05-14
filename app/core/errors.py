class ZorHubError(Exception):
    """Base exception for ZorHUB."""


class ConfigError(ZorHubError):
    """Raised when configuration cannot be loaded or saved."""


class MetricsError(ZorHubError):
    """Raised when a system metric cannot be read."""


class ComponentError(ZorHubError):
    """Raised when a component cannot be detected or loaded."""


class ActionError(ZorHubError):
    """Raised when a declared safe action cannot be executed."""


class UnsafeActionError(ZorHubError):
    """Raised when something tries to perform an unsafe action."""
