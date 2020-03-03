from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))


setup(
    name='ds_se_do',
    version='0.2.0',
    description='Data Science (ds) - Software Engineering (se) - DevOps (do)',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires='>=3.6, <4',
    install_requires=[],
    extras_require={},
    package_data={},
    entry_points={},
)
