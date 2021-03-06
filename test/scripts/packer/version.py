#!/usr/bin/env python3

# local
import lib.packer


# =============================================================================
#
# private test functions
#
# =============================================================================

# =============================================================================
# _test__version
# =============================================================================
def _test__version() -> dict:
    lib.packer.version()


# =============================================================================
#
# general
#
# =============================================================================

# =============================================================================
# do_test
# =============================================================================
def do_test() -> None:
    _test__version()


# =============================================================================
#
# main
#
# =============================================================================

if __name__ == "__main__":
    do_test()
