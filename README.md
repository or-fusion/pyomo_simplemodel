[![Build Status](https://travis-ci.org/Pyomo/pyomo_simplemodel.svg?branch=master)](https://travis-ci.org/Pyomo/pyomo_simplemodel)
[![Build status](https://ci.appveyor.com/api/projects/status/a3o40900jlx6x6jx?svg=true)](https://ci.appveyor.com/project/WilliamHart/pyomo-simplemodel)

## Overview

### Description 
The **pyomo_simplemodel** package is software for modeling
and solving optimization problems.  This package is derived from
[Pyomo](http://www.pyomo.org), and it provides functionality that
is comparable to [PuLP](https://github.com/coin-or/pulp).  This
software is available under the BSD License.

This software defines the **SimpleModel** class, which illustrates
how Pyomo can be used in a simple, less object-oriented manner.
Specifically, this class mimics the modeling style supported by
PuLP. Here is a comparison of features between PuLP and SimpleModel:

| Feature | PuLP | SimpleModel |
|:---------|------:|-------------:|
|LP/MILP  | YES  | YES         |
| NLP/MINLP | NO | YES |
|Column-wise | YES | NO |

The **SimpleModel** class illustrates the basic steps in
formulating and solving an optimization problem, but it is not meant
to serve as a replacement for Pyomo.  Pyomo models supports a much
richer set of modeling components than simple objectives and
constraints.  In particular, the **Block** component supports the
expression of hierarchical models with nested structure.  The
**SimpleModel** class only supports a simple, non-hierarchical optimization problems.

### Developers

By contributing to this software project, you are agreeing to the
following terms and conditions for your contributions:

1. You agree your contributions are submitted under the BSD license. 
2. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer. 
