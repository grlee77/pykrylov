"""Conjugate-Gradient Squared Algorithm"""

# Ideally, tfqmr should be a subpackage of cgs but how do you do that with
# distutils without having tfqmr in a subdirectory of cgs???

from .cgs import *

__all__ = [s for s in dir() if not s.startswith('_')]
