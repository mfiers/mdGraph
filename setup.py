#!/usr/bin/env python

import os
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

# see:
# http://groups.google.com/group/comp.lang.python/browse_thread/\
#      thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

DESCRIPTION = """
mdGraph

a tiny plugin for python markdown that converts certain markdown
tables to google chart api plots
""".strip()
 
setup(name='mdGraph',
      version='0.1',
      description=DESCRIPTION,
      author='Mark Fiers',
      author_email='mark.fiers42@gmail.com',
      url='http://mfiers.github.com/Moa/api/fist.html',
      packages=['mdx_mdGraph', ],
      package_dir = {'mdx_mdGraph': './mdx_mdGraph'},
      requires = [],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          ]
     )
