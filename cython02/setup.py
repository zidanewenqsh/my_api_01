# file: setup.py
# from distutils.core import setup
# from Cython.Build import cythonize
'''python setup.py build_ext --inplace'''
# setup(name='Hello world app',
#       ext_modules=cythonize("hello.pyx"))
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

filename = 'hello'  # 源文件名
full_filename = 'hello.pyx'  # 包含后缀的源文件名

# ext_modules = [Extension(filename, sources=[full_filename, "main.c"], include_dirs=[numpy.get_include()])]
ext_modules=cythonize("hello.pyx")
setup(
    name='hello',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
