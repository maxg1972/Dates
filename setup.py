from setuptools import setup
from distutils.core import setup

settings = dict()

setup(
    name='Dates',
    version='1.1.1',
    description='Utilities to facilitate date and time handling',
    long_description=open('README.md').read(),
    author='Massimo Guidi',
    author_email='maxg1972@gmail.com',
    url='https://github.com/maxg1972/Dates',
    py_modules=['Dates'],
    package_data={'': ['README.md']},
    include_package_data=True,
    install_requires=['datetime'],
    tests_require=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python License (CNRI Python License)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
