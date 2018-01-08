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
import pprint


def log(msg):
    sys.stderr.write(msg + '\n')
    return


def parse_input(req):
    log('parse input')
    ns = req['source']['ns']
    bucket = req['source']['bucket']
    version = req.get('version', None)
    regexp = req['source'].get('regexp', '')
    log('ns = '+ns+', bucket='+bucket+' v='+pprint.pformat(version, indent=4)+' re='+regexp)

    if version:
        version = version.get('version', None)
    log('v1 ='+pprint.pformat(version))
    return [ns, bucket, version, regexp]


def is_match(filename, regex):
    return re.match(regex, filename)


def get_prefix(filename):
    prefix_regexp = re.compile("^[-\w]+")
    prefix = None

    match = prefix_regexp.match(filename)
    if match:
        prefix = match.group(0)

    return prefix
