# from distutils.core import setup
# from Cython.Build import cythonize
# from Cython.Distutils import build_ext
# from distutils.extension import Extension
#
# setup(
#     cmdclass={'build_ext': build_ext},
#     ext_modules=[Extension("calculate", ["cythonfn.pyx"])]
# )

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
setup(
cmdclass = {'build_ext': build_ext},
ext_modules = [Extension("calculate", ["cythonfn.pyx"])]
)


# filename = 'test'  # 源文件名
# full_filename = 'test.pyx'  # 包含后缀的源文件名
#
# ext_modules = [Extension(filename, sources=[full_filename, "main.c"], include_dirs=[numpy.get_include()])]
# setup(
#     name='test',
#     cmdclass={'build_ext': build_ext},
#     ext_modules=ext_modules
# )
