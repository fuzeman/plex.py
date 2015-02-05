from plex import __version__

from setuptools import setup, find_packages

setup(
    name='plex.py',
    version=__version__,
    license='MIT',
    url='https://github.com/fuzeman/plex.py',

    author='Dean Gardiner',
    author_email='me@dgardiner.net',

    description='Python interface for the Plex Media Server API',
    packages=find_packages(exclude=[
        'examples',
        'tests'
    ]),
    platforms='any',

    install_requires=[
        'requests'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
