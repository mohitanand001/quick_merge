import sys

from setuptools import find_packages, setup

setup(
    name="quick_merge",
    version="0.0.1",
    description="Quickly merge files in bulk.",
    maintainer="Mohit Anand",
    maintainer_email="anand.mohit001@gmail.com",
    url="https://github.com/farziengineer/quick_merge",
    platforms="any",
    packages=["quick_merge",],
    keywords=["pandas"],
    install_requires=["pandas"],
)
