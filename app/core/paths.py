from pathlib import Path
from platformdirs import user_config_dir, user_data_dir, user_cache_dir, user_log_dir

from app.core.version import APP_NAME

CONFIG_DIR = Path(user_config_dir(APP_NAME, appauthor=False))
DATA_DIR = Path(user_data_dir(APP_NAME, appauthor=False))
CACHE_DIR = Path(user_cache_dir(APP_NAME, appauthor=False))
LOG_DIR = Path(user_log_dir(APP_NAME, appauthor=False))

CONFIG_FILE = CONFIG_DIR / "config.json"
HISTORY_FILE = DATA_DIR / "history.jsonl"
LOG_FILE = LOG_DIR / "zorhub.log"


def ensure_app_dirs() -> None:
    """Create required user-level directories."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
