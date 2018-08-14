# -*- coding: utf-8 -*-
"""
    descriptive_meta_tags
    ~~~~~~~~~~~~~~~~~~~~~

    Detect when the forum is being crawled, inject descriptive meta tags so that embeds look pretty.

    :copyright: (c) 2018 by Михаил Лебедев.
    :license: BSD License, see LICENSE for more details.
"""
import ast
import re
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("descriptive_meta_tags/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


setup(
    name="flaskbb-plugin-descriptive_meta_tags",
    version=version,
    url="https://flaskbb.org",
    license="BSD License",
    author="Михаил Лебедев",
    author_email="micha030201@gmail.com",
    description="Detect when the forum is being crawled, inject descriptive meta tags so that embeds look pretty.",
    long_description=__doc__,
    keywords="flaskbb plugin",
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["descriptive_meta_tags/translations/*/*/*.mo",
             "descriptive_meta_tags/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "descriptive-meta-tags = descriptive_meta_tags"
        ]
    },
    install_requires=[
        "FlaskBB"  # pin to a version to has pluggy integration
    ],
    setup_requires=[
        "Babel",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
