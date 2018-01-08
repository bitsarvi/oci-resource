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

from . import object_common

from distutils.version import LooseVersion
import re
import os
import oci


def get_oci_config(req):
    cwd = os.getcwd()
    key_file = cwd + '/oci_api_key.pem'
    f = open(key_file, "w")
    f.write(req['source']['apikey'])
    f.close()
    config = {
        "user": req['source']['user'],
        "key_file": key_file,
        "fingerprint": req['source']['fingerprint'],
        "tenancy": req['source']['tenancy'],
        "region": req['source']['region'],
    }
    oci.config.validate_config(config)
    return config


def get_oci_client(req):
    config = get_oci_config(req)
    return oci.object_storage.ObjectStorageClient(config)


def get_versions(req):
    client = get_oci_client(req)
    ns, bucket, version, regexp = object_common.parse_input(req)
    if len(regexp) == 0:
        raise ValueError("regexp cannot be empty")

    latest = None
    if version:
        latest = version['path']

    prefix = object_common.get_prefix(regexp)

    response = client.list_objects(ns, bucket, prefix=prefix)
    versions = []
    if response and len(response.data.objects):
        pattern = re.compile(regexp)
        for o in response.data.objects:
            m = pattern.match(o.name)
            if m:
                if len(m.groups()) == 1:
                    v = m.group(1)
                    if not latest or LooseVersion(o.name) >= LooseVersion(latest):
                        # metadata = [{'name': 'filename', 'value': o.name}, {'name': 'version', 'value': v}]
                        # versions.append({'path': o.name, 'metadata': metadata})
                        versions.append({'version': o.name})
        if len(versions) > 0:
            versions = sorted(versions, key=lambda x: LooseVersion(x['version']), reverse=False)
    # object_common.log(pprint.pformat(versions, indent=4))
    return versions


def get_object(req, name):
    client = get_oci_client(req)
    ns = req['source']['ns']
    bucket = req['source']['bucket']
