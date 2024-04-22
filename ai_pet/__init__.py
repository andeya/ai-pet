# type: ignore[attr-defined]
"""
Awesome `ai-pet` is a AI pet chat application.

Top-level package for ai_pet.
"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

__email__ = "andeyalee@outlook.com"


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
