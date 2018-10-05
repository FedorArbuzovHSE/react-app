#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="greetings",
    version="0.0.0",
    author="Fedor Arbuzov",
    author_email="arbuzovfp@gmail.com",
    url="https://github.com/FedorArbuzov/awesome",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)