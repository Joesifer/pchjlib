# pchjicon.py

"""
PCHJLIB😺
================================================================================================
------------------------------------------------------------------------------------------------
Author
------------------------------------------------------------------------------------------------
- Joesifer.

Version
------------------------------------------------------------------------------------------------
- 1.4.5.

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
  >>> Link: https://github.com/Joesifer/pchjlib/blob/main/README.md

Feedback and support are welcome via:
  >>> Email: phanchanhung12055@gmail.com

THANK YOU!!!
================================================================================================
"""

import sys, ctypes, importlib.resources


def main():
    if sys.platform != "win32":
        print("This feature only runs on Windows.")
        sys.exit(1)

    try:
        with importlib.resources.path("pchjlib", "desktop.ini") as ini_path:
            pkg_dir = ini_path.parent
            ini_file = ini_path
    except Exception as e:
        print(f"Error determining package path: {e}")
        sys.exit(1)

    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_SYSTEM = 0x04

    ctypes.windll.kernel32.SetFileAttributesW(str(pkg_dir), FILE_ATTRIBUTE_SYSTEM)
    attrs = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
    ctypes.windll.kernel32.SetFileAttributesW(str(ini_file), attrs)

    print(f"Icon has been applied to the folder: {pkg_dir}")


if __name__ == "__main__":
    main()
