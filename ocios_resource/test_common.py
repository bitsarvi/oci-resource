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

from . import object_common


class TestCommon(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_match(self):
        self.assertTrue(object_common.is_match("foobar.txt", "foobar\.txt"))
        regexp = "cpi-([0-9]+\.[0-9]+\.[0-9]+)\.tar.gz"
        self.assertTrue(object_common.is_match("cpi-1.0.0.tar.gz", regexp))
        self.assertFalse(object_common.is_match("CPI-1.0.0.tar.gz", regexp))
        self.assertFalse(object_common.is_match("cpi-1.0.0.tgz", regexp))
        self.assertFalse(object_common.is_match("cpi-10.0.tar.gz", regexp))

    def test_get_prefix(self):
        self.assertEquals(object_common.get_prefix('foobar'), 'foobar')
        self.assertEquals(object_common.get_prefix('foo(bar'), 'foo')
        self.assertEquals(object_common.get_prefix('foo.bar'), 'foo')
        self.assertEquals(object_common.get_prefix('123_abc'), '123_abc')
        self.assertEquals(object_common.get_prefix('foo-1234'), 'foo-1234')
        self.assertEquals(object_common.get_prefix('foo-([0-9])-1234'), 'foo-')
        self.assertEquals(object_common.get_prefix('([0-9])-1234'), None)


if __name__ == '__main__':
    unittest.main()
