class ZorHubError(Exception):
    """Base exception for ZorHUB."""


class ConfigError(ZorHubError):
    """Raised when configuration cannot be loaded or saved."""


class MetricsError(ZorHubError):
    """Raised when a system metric cannot be read."""


class ComponentError(ZorHubError):
    """Raised when a component cannot be detected or loaded."""


class UnsafeActionError(ZorHubError):
    """
    Raised when something tries to perform an unsafe action.

    In pα0.1 this should almost never happen, because privileged
    actions are not implemented.
    """