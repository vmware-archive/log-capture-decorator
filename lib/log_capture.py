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

from __future__ import print_function

import os
import sys
import json

def main():
	stream = sys.argv[1]
	print("Capturing logs on {}".format(stream))

	appinfo = get_application_info()
	service = find_logdrain_service(appinfo)
	if service != None:
		while True:
			line = sys.stdin.readline()
			# on push, sys.stdin reads tons of blank lines
			if line.strip() != "":
				if stream == 'stderr':
					print('[log-capture on {}]'.format(stream), line, file=sys.stderr)
				else:
					print('[log-capture on {}]'.format(stream), line, file=sys.stdout)

def detect():
	appinfo = get_application_info()
	service = find_logdrain_service(appinfo)
	if service == None:
		sys.exit(1)
	else:
		print('log-capture')
		sys.exit(0)

# Get Application Info
#
# Collect information about the application that can be included
# in what's forwarded to the logdrain service (in a real implementation)
#
def get_application_info():
	appinfo = {}
	vcap_application = json.loads(os.getenv('VCAP_APPLICATION', '{}'))
	appinfo['name'] = vcap_application.get('application_name')
	if appinfo['name'] == None:
		print("VCAP_APPLICATION must specify application_name", file=sys.stderr)
		sys.exit(1)
	appinfo['instance'] = os.getenv('CF_INSTANCE_INDEX')
	appinfo['hostname'] = vcap_application.get('application_uris')[0]
	appinfo['ipaddress'] = os.getenv('CF_INSTANCE_IP')
	appinfo['port'] = os.getenv('CF_INSTANCE_PORT')
	return appinfo

# Find bound logdrain service
#
# Right now this just looks for any bound service instance with
# a tag 'logdrain'
#
def find_logdrain_service(appinfo):
	vcap_services = json.loads(os.getenv('VCAP_SERVICES', '{}'))
	for service in vcap_services:
		service_instances = vcap_services[service]
		for instance in service_instances:
			tags = instance.get('tags', []) + instance.get('credentials',{}).get('tags',[])
			if 'logdrain' in tags:
				return instance
	return None

if __name__ == "__main__":
	main()
