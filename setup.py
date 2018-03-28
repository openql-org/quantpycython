#!/usr/bin/env python

from os import path

dir_setup = path.dirname(path.realpath(__file__))
requires = []

from setuptools import setup, Command

modules = [
    ]

tests = [
    ]

long_description = '''QuantPyCython is the QuantPy library Plugin using Cython for quantum computing.
It aims to become extension library set of quantpy.'''

with open(path.join(dir_setup, 'quantpycython', 'release.py')) as f:
    # Defines __version__
    exec(f.read())


if __name__ == '__main__':
    setup(name='quantpycython',
        version=__version__,
        description='QuantPy Plugin using Cython, that extends quantum Executor/Simulator.',
        long_description=long_description,
        author='QuantPy development team',
        author_email='quantpy@openql.org',
        license='Apache 2.0',
        keywords="Math Physics quantum quantpy",
        url='http://quantpy.org',
        packages=['quantpycython'] + modules + tests,
        ext_modules=[],
        classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Scientific/Engineering :: Physics',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            ],
        install_requires=requires,
        )

    from distutils.core import setup
    from distutils.extension import Extension
    from Cython.Distutils import build_ext
    import numpy
    import os
    if os.name=="posix":
        setup(
            cmdclass = {'build_ext': build_ext},
            ext_modules = [Extension("quantpycython.executor.simulator.cython_simulator", ["./quantpycython/executor/simulator/cython_simulator.pyx"],language='c')],
            include_dirs = [numpy.get_include()]
        )
        setup(
            cmdclass = {'build_ext': build_ext},
            ext_modules = [Extension("quantpycython.executor.simulator.cython_openmp_simulator", ["./quantpycython/executor/simulator/cython_openmp_simulator.pyx"],extra_compile_args=['-fopenmp'],extra_link_args=['-lgomp'],language='c')],
            include_dirs = [numpy.get_include()]
        )

    elif os.name=="nt":
        setup(
            cmdclass = {'build_ext': build_ext},
            ext_modules = [Extension(
                "quantpycython.executor.simulator.cython_simulator",
                ["./quantpycython/executor/simulator/cython_simulator.pyx"],
                extra_compile_args=['/Ot', '/favor:INTEL64', '/EHsc', '/GA'],
                language='c'
                )],
            include_dirs = [numpy.get_include()]
        )
        setup(
            cmdclass = {'build_ext': build_ext},
            ext_modules = [Extension(
                "quantpycython.executor.simulator.cython_openmp_simulator",
                ["./quantpycython/executor/simulator/cython_openmp_simulator.pyx"],
                extra_compile_args=['/Ot', '/favor:INTEL64', '/EHsc', '/GA', '/openmp'],
                language='c'
                )],
            include_dirs = [numpy.get_include()]
        )
