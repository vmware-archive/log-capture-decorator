#!/usr/bin/env bash

# log-capture-decorator
#
# Copyright (c) 2017-Present Pivotal Software, Inc. All Rights Reserved.
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

# These magic incantations cause all stdout and stderr messages from
# the remainder of this process tree to be sent to our log_capture.py
# sidecar processes. In this particular example, those in turn echo
# back to stdout and stderr with a prefix to show that the log capture
# worked. A real implementation of the sidecar might forward the messages
# to a log drain, and make the echo-back optional.

exec  > >(python $DEPS_DIR/__BUILDPACK_INDEX__/log_capture.py stdout)
exec 2> >(python $DEPS_DIR/__BUILDPACK_INDEX__/log_capture.py stderr)
