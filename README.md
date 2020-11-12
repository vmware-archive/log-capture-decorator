# log-capture-decorator is no longer actively maintained by VMware.

# Log Capture Decorator

This is a sidecar for multi-buildpack. When used, all log messages will have a prefix. 

The log handling sidecar process is a minimal Python implementation for demonstration purposes only. A real
implementation would replace it with the appropriate agent code.

## Use

This example requires opting in via multi-buildpack and a v3 push 

```bash
cf v3-push yay -b log-capture-buildpack -b python_buildpack
```

Example of the buildpack working as it manipulates the logs with `cf logs MY_APP`:
```
-07-18T06:38:04.53-0700 [CELL/0]     OUT Successfully created container
2017-07-18T06:38:06.23-0700 [STG/0]      OUT Successfully destroyed container
2017-07-18T06:38:06.96-0700 [CELL/0]     OUT Starting health monitoring of container
2017-07-18T06:38:07.09-0700 [APP/PROC/WEB/0]OUT Capturing logs on stdout
2017-07-18T06:38:07.10-0700 [APP/PROC/WEB/0]OUT [log-capture on stdout] Capturing logs on stderr
2017-07-18T06:38:07.35-0700 [APP/PROC/WEB/0]OUT [log-capture on stdout] Listening on port [8080]
2017-07-18T06:38:07.36-0700 [APP/PROC/WEB/0]ERR [log-capture on stderr]  * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
2017-07-18T06:38:09.03-0700 [CELL/0]     OUT Container became healthy
2017-07-18T06:40:11.97-0700 [RTR/0]      OUT app-python-flask.cfapps.example.com - [2017-07-18T13:40:11.968+0000] "GET / HTTP/1.1" 200 0 23 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36" "130.211.0.214:60366" "192.168.16.25:61014" x_forwarded_for:"64.125.192.130, 130.211.33.29" x_forwarded_proto:"http" vcap_request_id:"c350860a-5dcc-4096-4990-d825518808b3" response_time:0.003364407 app_id:"aa1613f7-bd49-4004-8d17-229b471ff18b" app_index:"0" x_b3_traceid:"5182d65305b74ca0" x_b3_spanid:"5182d65305b74ca0" x_b3_parentspanid:"-"
2017-07-18T06:40:11.97-0700 [APP/PROC/WEB/0]OUT [log-capture on stdout] {"success": false, "hello": "world", "foo": 1}
2017-07-18T06:40:11.97-0700 [APP/PROC/WEB/0]ERR [log-capture on stderr] 192.168.16.18 - - [18/Jul/2017 13:40:11] "GET / HTTP/1.1" 200 -
2017-07-18T06:40:38.83-0700 [APP/PROC/WEB/0]OUT [log-capture on stdout] {"success": false, "hello": "world", "foo": 2}
2017-07-18T06:40:38.83-0700 [APP/PROC/WEB/0]ERR [log-capture on stderr] 192.168.16.18 - - [18/Jul/2017 13:40:38] "GET / HTTP/1.1" 200 -
2017-07-18T06:40:38.84-0700 [RTR/0]      OUT app-python-flask.cfapps.example.com - [2017-07-18T13:40:38.836+0000] "GET / HTTP/1.1" 200 0 23 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36" "130.211.0.214:60366" "192.168.16.25:61014" x_forwarded_for:"64.125.192.130, 130.211.33.29" x_forwarded_proto:"http" vcap_request_id:"ebce710a-c253-4e06-75fd-e95d88b4cf05" response_time:0.003325463 app_id:"aa1613f7-bd49-4004-8d17-229b471ff18b" app_index:"0" x_b3_traceid:"12fb4e42b2e77a4c" x_b3_spanid:"12fb4e42b2e77a4c" x_b3_parentspanid:"-"
```

## Resources
See https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html for buildpack basics. 
This is an intermediate buildpack using only the bin/supply script.

See https://docs.cloudfoundry.org/buildpacks/use-multiple-buildpacks.html#Specifying%20Buildpacks%20with%20the%20cf%20CLI 
for information about pushing an application with multiple buildpacks.
