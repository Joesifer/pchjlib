import sys, ctypes, importlib
from pathlib import Path


def main():
    if sys.platform != "win32":
        print("This feature only runs on Windows.")
        sys.exit(1)

    pkg = importlib.import_module("pchjlib")
    file_path = getattr(pkg, "__file__", None)
    if not file_path:
        print("Package path not determined.")
        sys.exit(1)

    pkg_dir = Path(file_path).parent
    ini_file = pkg_dir / "desktop.ini"

    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_SYSTEM = 0x04

    ctypes.windll.kernel32.SetFileAttributesW(str(pkg_dir), FILE_ATTRIBUTE_SYSTEM)
    attrs = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
    ctypes.windll.kernel32.SetFileAttributesW(str(ini_file), attrs)

    print(f"Icon has been applied to the folder: {pkg_dir}")


if __name__ == "__main__":
    main()
