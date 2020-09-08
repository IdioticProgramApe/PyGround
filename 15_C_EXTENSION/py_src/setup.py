from distutils.core import setup, Extension


setup(
    name='sample',
    ext_modules=[
        Extension(
            'sample',
            ['sample/python_api/extension.c'],
            include_dirs=['sample/python_api'],
            define_macros=[],
            undef_macros=[],
            library_dirs=['sample/x64/Release'],
            libraries=['python_api']
        )
    ]
)