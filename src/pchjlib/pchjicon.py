# pchjicon.py

"""
PCHJLIB😺
================================================================================================

>>> Apply an icon to a folder (currently only supported on Windows).
>>> For detailed instructions, please see the `README.md` file.

================================================================================================
"""

import sys, ctypes, importlib.resources


def main():
    if sys.platform != "win32":
        print("This feature only runs on Windows.")
        sys.exit(1)

    print(
        "Warning: This will modify folder attributes (set system/hidden) and apply icon. Continue? [y/n]"
    )
    response = input().strip().lower()
    if response != "y":
        print("Operation cancelled.")
        sys.exit(0)

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
