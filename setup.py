#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy


# for fast spearman
ext_modules = [Extension('dstools.spearmanr_by_fast',
    sources=["dstools/spearmanr_by_fast.pyx", "dstools/cspearmanr_by_fast.cc"],
    include_dirs = [numpy.get_include()],
    language="c++",
    )]

setup(
    name             = 'dstools',
    version          = '0.0.1',
    description      = 'Data science tools',
    author           = 'Jackson Feng',
    author_email     = 'jackson.feng.wa@gmail.com',
    packages         = ['dstools', 'dstools.models', 'dstools.glm'],
    license          = 'MIT',
    platforms        = 'Posix; MacOS X',
    cmdclass         = {'build_ext': build_ext},
    ext_modules      = ext_modules,
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Science/Research'
        ],
)
