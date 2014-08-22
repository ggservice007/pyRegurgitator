#! /usr/bin/env python

from setuptools import setup

# use README file as long_description
readme = open('README')
long_description = readme.read()
readme.close()


setup(name = 'pyRegurgitator',
      description = 'pyRegurgitator - Tools for analysing python code',
      version = '0.2.dev0',
      license = 'MIT',
      author = 'Eduardo Naufel Schettino',
      author_email = 'schettino72@gmail.com',
      url = 'http://github.com/schettino72/pyregurgitator/',
      classifiers = ['Development Status :: 3 - Alpha',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Operating System :: POSIX',
                     'Programming Language :: Python :: 3.3',
                     'Topic :: Software Development',
                     ],

      packages = ['regurgitator', 'regurgitator/project'],
      scripts = ['bin/ast2html', 'bin/pymap'],
      long_description = long_description,
      )

