# Copyright (c) 2018 LG Electronics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python
import json
import os.path

topdir = '.'
exten = '.json'
file_count = 0
error_count = 0

def step(ext, dirname, names):
    global file_count
    global error_count

    ext = ext.lower()

    for name in names:
        if name.lower().endswith(ext):
            file_count += 1
            json_filename = os.path.join(dirname, name)
            try:
                with open(json_filename) as json_data:
                    json_object = json.load(json_data)
            except ValueError, e:
                error_count += 1
                print json_filename
                print "    ", e

# Start the walk
os.path.walk(topdir, step, exten)

print "Errors:", error_count, ", Files:", file_count
