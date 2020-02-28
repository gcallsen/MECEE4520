from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))


setup(
    name='class_demo',
    version='0.1.0',
    description='Class Demo Project',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires='>=3.6, <4',
    install_requires=[],
    extras_require={},
    package_data={},
    entry_points={},
)
