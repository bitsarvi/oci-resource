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

from . import object_in


class TestIn(unittest.TestCase):
    def setUp(self):
        with open(os.environ['OCI_CONFIG'], "r") as f:
            self.srcdata = json.load(f)
            f.close()
        with open(os.environ['OCI_KEYFILE'], "r") as f:
            apikey = f.read()
            f.close()
        self.srcdata['apikey'] = apikey
        self.srcdata['ns'] = 'cloudfoundry'

    def test_in(self):
        self.srcdata['bucket'] = 'test'
        filespec = {"path": "test-2.txt"}
        args = {
            'source': self.srcdata,
            'version': filespec
        }
        self.assertEquals(object_in.object_in(".", args), filespec)


if __name__ == '__main__':
    unittest.main()
