#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Blockstore
    ~~~~~
    copyright: (c) 2014-2015 by Halfmoon Labs, Inc.
    copyright: (c) 2016 by Blockstack.org

    This file is part of Blockstore

    Blockstore is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Blockstore is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with Blockstore. If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages
import sys
import os

sys.path.insert( 0, os.path.abspath( os.path.dirname(__file__) ) )
from blockstore.lib.config import VERSION

setup(
    name='blockstore',
    version=VERSION,
    url='https://github.com/blockstack/blockstore',
    license='GPLv3',
    author='Blockstack.org',
    author_email='support@blockstack.org',
    description='Name registrations on the Bitcoin blockchain with external storage',
    keywords='blockchain bitcoin btc cryptocurrency name key value store data',
    packages=find_packages(),
    scripts=['bin/blockstored'],
    download_url='https://github.com/blockstack/blockstore/archive/master.zip',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'virtualchain>=0.0.6',
        'kademlia>=0.5',
        'keychain>=0.1.4',
        'blockstore-client>=0.0.9',
        'base58=>0.2.2',
        'bitcoin>=1.1.39',
        'basicrpc>=0.0.2',
        'boto>=2.38.0',
        'commontools>=0.1.0',
        'ecdsa==0.13',
        'pybitcoin>=0.9.8',
        'requests>=2.8.1',
        'six>=1.10.0',
        'Twisted>=15.4.0',
        'txJSON-RPC>=0.3.1',
        'utilitybelt>=0.2.6',
        'virtualchain>=0.0.5'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
