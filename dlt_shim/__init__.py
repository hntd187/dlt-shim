try:
    import dlt
except (ImportError, ModuleNotFoundError):
    from .shim import *
    import sys

    sys.modules['dlt'] = shim

from dlt import *

__all__ = [
    "create_view",
    "create_table",
    "create_streaming_live_table",
    "create_streaming_table",
    "create_target_table",
    "view",
    "table",
    "read",
    "read_stream",
    "expect",
    "expect_or_fail",
    "expect_or_drop",
    "expect_all_or_fail",
    "expect_all_or_drop",
    "expect_all",
    "apply_changes"
]
