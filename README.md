[![Build Status](https://travis-ci.org/Pyomo/pyomocontrib_simplemodel.svg?branch=master)](https://travis-ci.org/Pyomo/pyomocontrib_simplemodel)
[![Build status](https://ci.appveyor.com/api/projects/status/urr88klp2dxsr5bt?svg=true)](https://ci.appveyor.com/project/WilliamHart/pyomocontrib-simplemodel)
[![Documentation Status](https://readthedocs.org/projects/pyomocontrib-simplemodel/badge/?version=latest)](http://pyomocontrib-simplemodel.readthedocs.org/en/latest/)

[![GitHub contributors](https://img.shields.io/github/contributors/pyomo/pyomocontrib_simplemodel.svg)](https://github.com/pyomo/pyomocontrib_simplemodel/graphs/contributors)
[![Merged PRs](https://img.shields.io/github/issues-pr-closed-raw/pyomo/pyomocontrib_simplemodel.svg?label=merged+PRs)](https://github.com/pyomo/pyomocontrib_simplemodel/pulls?q=is:pr+is:merged)
[![Issue stats](http://isitmaintained.com/badge/resolution/pyomo/pyomocontrib_simplemodel.svg)](http://isitmaintained.com/project/pyomo/pyomocontrib_simplemodel)
[![Research software impact](http://depsy.org/api/package/pypi/pyomocontrib_simplemodel/badge.svg)](http://depsy.org/package/python/pyomocontrib_simplemodel)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)

## Overview

### Description 
The **pyomocontrib_simplemodel** package is software for modeling
and solving optimization problems.  This package is derived from
[Pyomo](http://www.pyomo.org), and it defines the class **SimpleModel** that illustrates
how Pyomo can be used in a simple, less object-oriented manner.
Specifically, this class mimics the modeling style supported by
[PuLP](https://github.com/coin-or/pulp):

| Feature | PuLP | SimpleModel |
|:---------|------:|-------------:|
|LP/MILP  | YES  | YES         |
| NLP/MINLP | NO | YES |
|Column-wise | YES | NO |

[See the online documentation for further details.](http://pyomocontrib-simplemodel.readthedocs.org/en/latest/)

This software is available under the BSD License.

### Developers

By contributing to this software project, you are agreeing to the
following terms and conditions for your contributions:

1. You agree your contributions are submitted under the BSD license. 
2. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer. 
