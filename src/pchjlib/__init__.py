# __init__.py

################################################################################################
#
# Copyright (c) 2024 Joesifer
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
################################################################################################

"""
PCHJLIB😺
================================================================================================

Usage
------------------------------------------------------------------------------------------------
``` python

from pchjlib.pchjmain import is_prime
result = is_prime(7)  # Check for prime numbers

```
- For detailed instructions, please see the README.md file.

Author
------------------------------------------------------------------------------------------------
- Joesifer.

Version
------------------------------------------------------------------------------------------------
- 1.6.0.

Release Date
------------------------------------------------------------------------------------------------
- February 14, 2024.

License
------------------------------------------------------------------------------------------------
- Copyright © 2024 Joesifer

Supported Python Version
------------------------------------------------------------------------------------------------
- Python 3.7 or higher.

Dependencies
------------------------------------------------------------------------------------------------
- Built-in: `math`, `re`, `random`, `functools`, `argparse`.
- External: `gmpy2` (optional for big integer support).

License Type
------------------------------------------------------------------------------------------------
- MIT License.

Additional Information
------------------------------------------------------------------------------------------------

For usage instructions, please refer to:
>>> Link: https://github.com/Joesifer/pchjlib/blob/main/README.md

Feedback and support are welcome via:
>>> Email: phanchanhung12055@gmail.com

THANK YOU!!!
================================================================================================
"""


from importlib.metadata import version
from .pchjicon import main as pchj_icon
from .pchjmain import main as pchj_main
from .primes import *
from .twin_abundant import *
from .fibonacci import *
from .special_numbers1 import *
from .special_numbers2 import *
from .divisors_multiples import *
from .prime_factorization import *
from .string_processing import *
from .caesar_cipher import *
from .special_calculations import *
from .sequence_generation import *
from .inversion_counting import *

author = "Joesifer (phanchanhung12055@gmail.com)"
copyright = "Copyright (c) 2024 Joesifer"
version = version("pchjlib")
license = "MIT License"
release_date = "February 14, 2024"

all = [
    "primes",
    "twin_abundant",
    "fibonacci",
    "special_numbers1",
    "special_numbers2",
    "divisors_multiples",
    "prime_factorization",
    "string_processing",
    "caesar_cipher",
    "special_calculations",
    "sequence_generation",
    "inversion_counting",
    "pchj_main",
    "pchj_icon",
    "version",
    "author",
    "copyright",
    "license",
    "release_date",
]
