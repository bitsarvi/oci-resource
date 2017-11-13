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

import re
import sys

def log(msg):
    sys.stderr.write(msg + '\n')
    return

def parse_input(input):
    ns = input['source']['ns']
    bucket = input['source']['bucket']
    version = None
    if ('version' in input.keys()) and ('version' in input['version'].keys()):
        version = input['version']['version']
    regexp = ''
    if 'regexp' in input['source']:
        regexp = input['source']['regexp']
    return [ns, bucket, version, regexp]

def is_match(filename, regex):
    return re.match(regex, filename)

