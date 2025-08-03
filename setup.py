from setuptools import setup
from setuptools.command.install import install
import subprocess, os


class InstallWithIcon(install):
    def run(self):
        super().run()

        assert self.install_lib is not None
        install_lib = self.install_lib

        target = os.path.join(install_lib, "pchjlib")
        try:
            subprocess.run(["pchj-icon"], cwd=target, check=True)
        except Exception:
            print("Warning: pchj-icon failed, you can run manually after install")


setup(
    cmdclass={"install": InstallWithIcon},
)
