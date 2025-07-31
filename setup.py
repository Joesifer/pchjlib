# setup.py
################################################################################################
#                                                                                              #
# Copyright (c) 2024 Joesifer                                                                  #
#                                                                                              #
# MIT License                                                                                  #
#                                                                                              #
# Permission is hereby granted, free of charge, to any person obtaining a copy                 #
# of this software and associated documentation files (the "Software"), to deal                #
# in the Software without restriction, including without limitation the rights                 #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                    #
# copies of the Software, and to permit persons to whom the Software is                        #
# furnished to do so, subject to the following conditions:                                     #
#                                                                                              #
# The above copyright notice and this permission notice shall be included in all               #
# copies or substantial portions of the Software.                                              #
#                                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                #
# SOFTWARE.                                                                                    #
#                                                                                              #
################################################################################################

#!/usr/bin/env python
import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent
long_description = (HERE / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="pchjlib",
    version="0.1.1.1",
    author="Joesifer",
    description="Thư viện pchjlib là một bộ công cụ đa năng…",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joesifer/pchjlib",
    license="MIT",
    keywords="pchjlib",
    py_modules=["pchjlib"],
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "numpy": ["numpy"],
        "roman": ["roman"],
        "full": ["numpy", "roman"],
    },
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Natural Language :: Vietnamese",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "pchjlib = pchjlib:main",
        ]
    },
)
