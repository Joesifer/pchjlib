# setup.py
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
------------------------------------------------------------------------------------------------
Author
------------------------------------------------------------------------------------------------
- Joesifer.

Version
------------------------------------------------------------------------------------------------
- 1.4.0.

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
- External: `numpy` (optional for `solve_equation` and `generate_prime_list`).
- External (plan): `gmpy2` (optional for big integer support).

License Type
------------------------------------------------------------------------------------------------
- MIT License.

Additional Information
------------------------------------------------------------------------------------------------

For usage instructions, please refer to:
  >>> Link: `https://github.com/Joesifer/pchjlib/blob/main/README.md`

Feedback and support are welcome via:
  >>> Email: `phanchanhung12055@gmail.com`

THANK YOU!!!
================================================================================================
"""

from setuptools import setup
from setuptools.command.install import install
import subprocess, os


class InstallWithIcon(install):
    def run(self):
        super().run()
        assert self.install_lib is not None, "install_lib must be set"
        target = os.path.join(self.install_lib, "pchjlib")
        try:
            subprocess.run(["pchj-icon"], cwd=target, check=True)
        except subprocess.CalledProcessError:
            print("Warning: pchj-icon failed, you can run it manually")


if __name__ == "__main__":
    setup(cmdclass={"install": InstallWithIcon})
