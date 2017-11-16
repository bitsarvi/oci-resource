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

from . import object_common, ocios

import json
import os
import sys

def object_in(destdir, data):
    object_common.log('object_in')
    ns, bucket, version, regexp = object_common.parse_input(data)
    client = ocios.get_oci_client(data)
    obj = client.get_object(ns, bucket, "foo")
    version_dest = os.path.join(destdir, "file")
    with open(version_dest, "w") as f:
        f.write(obj.data)
    return version

def main():
    destdir = sys.argv[1]
    object_common.log('Output directory: {}'.format(destdir))
    version = object_in(destdir, json.load(sys.stdin))
    print(json.dumps({'version': {'version': version}}))

if __name__ == 'main':
    main()