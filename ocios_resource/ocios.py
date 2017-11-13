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
import os
import oci

def get_oci_config(input):
    cwd = os.getcwd()
    key_file = cwd + '/oci_api_key.pem'
    f = open(key_file, "w")
    f.write(input['source']['apikey'])
    f.close()
    config = {
        "user": input['source']['user'],
        "key_file": key_file,
        "fingerprint": input['source']['fingerprint'],
        "tenancy": input['source']['tenancy'],
        "region": input['source']['region'],
    }
    oci.config.validate_config(config)
    return config

def get_oci_client(input):
    config = get_oci_config(input)
    return oci.object_storage.ObjectStorageClient(config)

def get_object_list(input):
    client = get_oci_client(input)
    ns = input['source']['ns']
    bucket = input['source']['bucket']
    regex = input['source']['regexp']

    objects = client.list_objects(ns, bucket)
    return objects

def get_object(input, name):
    client = get_oci_client(input)
    ns = input['source']['ns']
    bucket = input['source']['bucket']









