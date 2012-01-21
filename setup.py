#!/usr/bin/env python

from setuptools import setup

setup(
    name="dom",
    version="0.1",
    description="An easy-to-use command line utility for domain name lookups.",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    url="http://github.com/zachwill/dom",
    license="MIT",
    packages=[
        "domainr"
    ],
    scripts=[
        "dom"
    ],
    install_requires=[
        "mock",
        "requests",
        "termcolor"
    ]
)
