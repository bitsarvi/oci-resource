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

import unittest
import json
import os

from . import object_check


class TestCheck(unittest.TestCase):
    def setUp(self):
        with open(os.environ['OCI_CONFIG'], "r") as f:
            self.srcdata = json.load(f)
            f.close()
        with open(os.environ['OCI_KEYFILE'], "r") as f:
            apikey = f.read()
            f.close()
        self.srcdata['apikey'] = apikey
        self.srcdata['ns'] = 'cloudfoundry'

    def test_nosuchfile(self):
        self.srcdata['bucket'] = 'test'
        self.srcdata['regexp'] = 'nosuchfile'
        args = {
            'source': self.srcdata
        }
        self.assertEquals(object_check.object_check(args), [])

        self.srcdata['bucket'] = 'test'
        self.srcdata['regexp'] = 'test-(\d+).txt'
        args = {
            'source': self.srcdata
        }
        self.assertEquals(len(object_check.object_check(args)), 3)

        self.srcdata['bucket'] = 'test'
        self.srcdata['regexp'] = 'test-(\d+).txt'
        args = {
            'source': self.srcdata,
            'version': {"path": "test-2.txt"}
        }
        self.assertEquals(len(object_check.object_check(args)), 2)



if __name__ == '__main__':
    unittest.main()
