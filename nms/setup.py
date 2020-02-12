from distutils.core import setup
from Cython.Build import cythonize

setup(
      name = 'mynms',
      ext_modules = cythonize('mynms.pyx'),
      )