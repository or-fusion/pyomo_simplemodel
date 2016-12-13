"""
Script to generate the installer for pyomo.aux.simplemodel
"""

import sys
import os


def _find_packages(path):
    """
    Generate a list of nested packages
    """
    pkg_list = []
    if not os.path.exists(path):
        return []
    if not os.path.exists(path+os.sep+"__init__.py"):
        return []
    else:
        pkg_list.append(path)
    for root, dirs, files in os.walk(path, topdown=True):
        if root in pkg_list and "__init__.py" in files:
            for name in dirs:
                if os.path.exists(root+os.sep+name+os.sep+"__init__.py"):
                    pkg_list.append(root+os.sep+name)
    return [pkg for pkg in map(lambda x:x.replace(os.sep, "."), pkg_list)]


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

requires = [
    'Pyomo>=5.0',
    ]

from setuptools import setup
packages = _find_packages('pyomocontrib_simplemodel')

setup(name='pyomocontrib_simplemodel',
      version='1.0.1',
      maintainer='William E. Hart',
      maintainer_email='wehart@sandia.gov',
      url='http://pyomo.org',
      license='BSD',
      platforms=["any"],
      description='An optimization modeling tool for LP and NLP',
      long_description=read('README.txt'),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Unix Shell',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ],
      packages=packages,
      keywords=['optimization'],
      install_requires=requires,
      )
