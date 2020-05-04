import numpy
import os, sys 
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

with open('requirements.txt', 'r') as fh:
    dependencies = [l.strip() for l in fh]


setup(
    name='PyRoss',
    version='1.0.0',
    url='https://gitlab.com/rajeshrinet/pyross',
    author='The PyRoss team',
    license='MIT',
    description='python library for numerical simulation of infectious disease',
    long_description='pyross is a library for numerical simulation of infectious disease',
    platforms='works on all platforms (such as LINUX, macOS, and Microsoft Windows)',
    ext_modules=cythonize([ Extension("pyross/*", ["pyross/*.pyx"],
        include_dirs=[numpy.get_include()],
        )],
        compiler_directives={"language_level": sys.version_info[0]},
        ),
    libraries=[],
    #install_requires=dependencies,
    #packages=find_packages(),
    packages=['pyross'],
    package_data={'': ['*pxd', '*xlsx']},
    include_package_data = True
)


