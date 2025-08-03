"""
PCHJLIB😺
===============================================================================
-------------------------------------------------------------------------------
Author
-------------------------------------------------------------------------------
- Joesifer.

Version
-------------------------------------------------------------------------------
- 1.0.1.

Release Date
-------------------------------------------------------------------------------
- August 3, 2025.

License
-------------------------------------------------------------------------------
- Copyright © 2024 Joesifer

Supported Python Version
-------------------------------------------------------------------------------
- Python 3.7 or higher.

Dependencies
-------------------------------------------------------------------------------
- Built-in: `math`, `re`, `random`, `functools`, `argparse`.
- External: `numpy` (optional for `solve_equation` and `generate_prime_list`).
- External (plan): `gmpy2` (optional for big integer support).

License Type
-------------------------------------------------------------------------------
- MIT License.

Additional Information
-------------------------------------------------------------------------------

For usage instructions, please refer to:
  >>> Link: https://github.com/Joesifer/pchjlib/blob/main/README.md

Feedback and support are welcome via:
  >>> Email: `phanchanhung12055@gmail.com`

THANK YOU!!!
===============================================================================
"""

from importlib.metadata import version
__version__ = version("pchjlib")

from .pchjlib import main
from .icon import main as icon_main

__all__ = ["main", "icon_main", "__version__"]
