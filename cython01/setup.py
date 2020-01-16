# import setuptools
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy as np

filename = 'test'  # 源文件名
full_filename = 'test.pyx'  # 包含后缀的源文件名

# ext_modules = [Extension(filename, sources=[full_filename, "main.c"], include_dirs=[numpy.get_include()])]
setup(
    name='test',
    cmdclass={'build_ext': build_ext},
    ext_modules= cythonize("test.pyx"),
    include_dirs=[np.get_include()]#不加这句会报：Cython fatal error C1083: 无法打开包括文件: “numpy/arrayobject.h”: No such file or directory
)
