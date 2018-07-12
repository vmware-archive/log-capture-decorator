# Log Capture Decorator

> <b>NOTE: Meta-buildback is being deprecated</b><br/>
> Changes to the core CloudFoundry lifecycle process are making it hard to guarantee
> on-going compatibility with meta-buildpack and decorators. Some of the use cases for
> decorators can now be solved by leveraging the new
> [supply buildpack](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html#supply-script)
> functionality. If you are using meta-buildpack today and need to find an alternative,
> or have a use case that would have been addressed by decorators, please open an issue
> on this repo and we are happy to help you look for the right way to accomplish your task.

This is a [decorator](https://github.com/cf-platform-eng/meta-buildpack/blob/master/README.md#decorators) buildpack
for Cloud Foundry that demonstrates how to capture application log information *for any programming
language* supported by the platform, and requiring *zero application code changes*.

When this decorator (and the [meta-buildpack](https://github.com/cf-platform-eng/meta-buildpack))
is present in your Cloud Foundry deployment, every application bound to an instance of a log drain service
will automatically have its stdout and stderr forwarded to that service. Unlike the loggregator subsystem,
this forwarding is lossless (but the trade-off is that it may block the application until log messages can
be delivered).

The log handling sidecar process is a minimal Python implementation for demonstration purposes only. A real
implementation would replace it with the appropriate agent code.


## Use

This example decorator is triggered by the presence of a tag `logdrain`. 

```bash
cf cups logdrain_trigger -p '{"tags":["logdrain"]}'
cf bind-service MY_APP logdrain_trigger
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
