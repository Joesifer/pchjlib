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


from setuptools import setup


with open(
    r"C:\Users\LAPTOP DELL\Desktop\pchjlib_admin\README.md", encoding="utf-8"
) as f:
    desc = f.read()

setup(
    name="pchjlib",
    version="0.0.4.1",
    author="Joesifer",
    description="Thư viện này có thể thực hiện các phép tính, thuật toán, xử lí chuỗi, mảng, . . .",
    long_description=desc,
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords="pchjlib",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
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
