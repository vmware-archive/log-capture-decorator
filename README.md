# Log Capture Decorator

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

