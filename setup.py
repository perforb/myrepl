# -*- coding: utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='myreplica',
    version='0.0.1',
    description='A tool that creates replica of MySQL tables or database.',
    long_description=readme,
    platforms=['linux', 'osx', 'unix'],
    packages=find_packages(exclude=('tests')),
    author='perforb',
    author_email='dev.perfurmed.garden@gmail.com',
    url='https://github.com/perforb/myreplica',
    license=license,
    keywords='mysql copy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database',
    ],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'myreplica=myreplica.myrepltb:main',
            'myreplica=myreplica.myrepldb:main',
        ],
    },
    test_suite='tests'
)
