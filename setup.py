#!/usr/bin/env python
#
# Setup script for units_and_physics module.
# Written by Patrick Varilly, 25 Jun 2012

import sys

if sys.version_info[0] >= 3:
    print "WARNING: units_and_physics package has not been tested on Python 3"

CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
Operating System :: Microsoft :: Windows
Programming Language :: Python
Topic :: Scientific/Engineering

"""

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(name="units_and_physics",
      version="1.0",
      author="Patrick Varilly",
      author_email="pv271@cam.ac.uk",
      description="Unit definitions and physical constants for molecular simulations",
      url="http://github.com/patvarilly/units_and_physics",
      license='GPLv3',
      classifiers=[_ for _ in CLASSIFIERS.split('\n') if _],
      platforms=["Linux", "Unix", "Mac OS-X", "Windows", "Solaris"],
      py_modules=['units', 'physics'],
      )
