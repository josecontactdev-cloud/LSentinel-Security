"""Utilities for cog helpers."""


def get_cog_name(cog_class):
    """Return the cog class name as a command group name."""
    return cog_class.__name__.replace("Cog", "").lower()
