#!/usr/bin/env python

# Copyright (c) 2017, Oracle and/or its affiliates. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

def read_readme():
    with open(os.path.join(here, 'README.md')) as f:
        return f.read()

def get_requirements():
    with open(os.path.join(here, 'requirements.txt')) as f:
        return f.readlines()

setup(
    name = "ocios-resource",
    version = '0.1.0',
    description = 'Concourse CI resource for OCI Object Store.',
    long_description = read_readme(),
    url = 'https://github.com/bitsarvi/ocios-resource',
    author = 'Oracle',
    license = 'Apache 2.0',
    classifiers = [
    ],
    keywords = [
    ],
    packages = [ 'ocios_resource' ],
    install_requires = get_requirements(),
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'check = ocios_resource.object_check:main',
            'in = ocios_resource.object_in:main',
            'out = ocios_resource.object_out:main',
        ]
    }
)
