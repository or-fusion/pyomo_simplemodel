
[![Actions Status](https://github.com/pyomocommunity/pyomo_simplemodel/workflows/continuous-integration/github/pr/linux/badge.svg)](https://github.com/pyomocommunity/pyomo_simplemodel/actions)
[![Documentation Status](https://readthedocs.org/projects/pyomo-simplemodel/badge/?version=latest)](http://pyomo-simplemodel.readthedocs.org/en/latest/)

[![Pyomo Checks - GitHub Master](https://github.com/pyomocommunity/pyomo_simplemodel/workflows/pyomo-checks/master/badge.svg)](https://github.com/pyomocommunity/pyomo_simplemodel/actions)
[![Pyomo Checks - PyPI](https://github.com/pyomocommunity/pyomo_simplemodel/workflows/pyomo-checks/pypi/badge.svg)](https://github.com/pyomocommunity/pyomo_simplemodel/actions)
[![Pyomo Checks - Conda](https://github.com/pyomocommunity/pyomo_simplemodel/workflows/pyomo-checks/conda/badge.svg)](https://github.com/pyomocommunity/pyomo_simplemodel/actions)

[![GitHub contributors](https://img.shields.io/github/contributors/pyomo/pyomo_simplemodel.svg)](https://github.com/pyomo/pyomo_simplemodel/graphs/contributors)
[![Merged PRs](https://img.shields.io/github/issues-pr-closed-raw/pyomo/pyomo_simplemodel.svg?label=merged+PRs)](https://github.com/pyomo/pyomo_simplemodel/pulls?q=is:pr+is:merged)
[![Issue stats](http://isitmaintained.com/badge/resolution/pyomo/pyomo_simplemodel.svg)](http://isitmaintained.com/project/pyomo/pyomo_simplemodel)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)

## Overview

### Description 
The **pyomo_simplemodel** package is software for modeling
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

[See the online documentation for further details.](http://pyomo-simplemodel.readthedocs.org/en/latest/)

This software is available under the BSD License.

### Installation

#### PyPI [![PyPI](https://img.shields.io/pypi/v/pyomo_simplemodel.svg?maxAge=2592000)]()
<!---
# PyPI download stats appear to be broken
[![PyPI](https://img.shields.io/pypi/dm/pyomo_simplemodel.svg?maxAge=2592000)]()
--->

    pip install pyomo_simplemodel
    
<!---
#### BinStar [![Binstar Badge](https://anaconda.org/conda-forge/pyomo_simplemodel/badges/version.svg)](https://anaconda.org/conda-forge/pyomo_simplemodel) [![Binstar Badge](https://anaconda.org/conda-forge/pyomo_simplemodel/badges/downloads.svg)](https://anaconda.org/conda-forge/pyomo_simplemodel)

    conda install -c https://conda.anaconda.org/conda-forge pyomo_simplemodel
--->

### Getting Help

* [Ask a Pyomo Question on StackExchange](https://stackoverflow.com/questions/ask?tags=pyomo)
* [Pyomo Forum](https://groups.google.com/forum/?hl=en#!forum/pyomo-forum)
* [Add a Ticket](https://github.com/Pyomo/pyomo_simplemodel/issues/new)
* [Find a Ticket](https://github.com/Pyomo/pyomo_simplemodel/issues) and **Vote On It**!


### Developers

By contributing to this software project, you are agreeing to the
following terms and conditions for your contributions:

1. You agree your contributions are submitted under the BSD license. 
2. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer. 
