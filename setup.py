from setuptools import setup, find_namespace_packages

setup(
    name='fampnn',
    version='0.1',
    packages=find_namespace_packages(include=['fampnn*', 'openfold*']),
    include_package_data=True,
    python_requires='>=3.9',
)
