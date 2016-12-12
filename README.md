[![Build Status](https://travis-ci.org/Pyomo/pyomo_simplemodel.svg?branch=master)](https://travis-ci.org/Pyomo/pyomo_simplemodel)
[![Build status](https://ci.appveyor.com/api/projects/status/a3o40900jlx6x6jx?svg=true)](https://ci.appveyor.com/project/WilliamHart/pyomo-simplemodel)
[![Documentation Status](https://readthedocs.org/projects/pyomo-simplemodel/badge/?version=latest)](http://pyomo-simplemodel.readthedocs.org/en/latest/)

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

Note that **pyomo_simplemodel** is not meant
to serve as a replacement for Pyomo.  Pyomo supports a much
richer set of modeling components than simple objectives and
constraints.  In particular, Pyomo's **Block** component supports the
expression of hierarchical models with nested structure, while **pyomo_simplemodel** only
supports a simple, non-hierarchical optimization problems.

This software is available under the BSD License.

### Developers

By contributing to this software project, you are agreeing to the
following terms and conditions for your contributions:

1. You agree your contributions are submitted under the BSD license. 
2. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer. 
