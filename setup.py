################################################################################################
#
# Copyright (c) 2024 Joesifer
# Any act of hitting a subordinate will result in a beating
# Supported python versions = {"all"}
# Imported library = {"cmath", "collections", "math", "re", "sys", "time", "numpy", "roman"}
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
################################################################################################

from setuptools import setup


desc = "{}\n\n{}".format(
    open(r"C:\Users\LAPTOP DELL\Desktop\pchjlib_admin\README.md").read(),
    open(r"C:\Users\LAPTOP DELL\Desktop\pchjlib_admin\CHANGES.md").read(),
)

setup(
    name="pchjlib",
    version="0.0.2.4",
    author="Joesifer",
    maintainer="Zope Foundation and Contributors",
    maintainer_email="zope-dev@zope.dev",
    description="Bộ sưu tầm hàm con của mình",
    long_description=desc,
    long_description_content_type="text/markdown",
    license="ZPL 2.1",
    keywords="pchjlib",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Natural Language :: Vietnamese",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Joesifer/pchjlib",
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=["numpy", "roman"],
    py_modules=["pchjlib"],
    include_package_data=True,
    test_suite="",
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "pchjlib=pchjlib:main",
        ]
    },
)
