# -*- coding: utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup

REQUIRES = [
]

setup(
    name='mycopier',
    version='0.0.1',
    description='A tool that copies data of MySQL tables.',
    platforms=['linux', 'osx', 'unix'],
    packages=['mycopier'],
    author='perforb',
    author_email='dev.perfurmed.garden@gmail.com',
    url='https://github.com/perforb/mycopier-python',
    license='MIT',
    keywords='mysql copy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database',
    ],
    install_requires=REQUIRES,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    tests_require=[
        'pytest',
        'pytest-pep8',
        'pytest-flakes',
        'tox',
        'mock',
    ],
    include_package_data=True,
    package_data={
    },
    data_files=[],
    entry_points={
        'console_scripts': [
            'mycopier=mycopier.excecutor:main',
        ],
    },
)
