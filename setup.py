from setuptools import setup, find_packages

setup(
    name='nestedlist',
    version='0.1.0',
    description='nestedlist.nested_list mimics with list the c style multi-dimensional array declaration. For example, `a=nested_list([12,6,7], int)` is like `int a[12][6][7];` in C. ',
    url="https://github.com/yssgo/nestedlist",
    packages=find_packages(),
)
