from distutils.core import setup
from Cython.Build import cythonize

try:
    setup(
        ext_modules=cythonize(
            "optimisedsimulation.pyx", compiler_directives={"language_level": "3"}
        )
    )
except:
    setup(
        ext_modules=cythonize(
            "lib/optimisedsimulation.pyx", compiler_directives={"language_level": "3"}
        )
    )

# to run
# python cysetup.py build_ext --inplace