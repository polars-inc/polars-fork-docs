# F.A.Q.

This page contains a number of frequently asked questions. Is your question not listed here? Please reach out to us on Discord or by email.

### Is Polars Cloud also available on Microsoft Azure / Google Cloud Platform / ... ?

The current version of Polars Cloud only supports Amazon Web Services (AWS). Support for other platforms is on the roadmap.

### Can I run Polars Cloud on my custom on-premise servers?

This is currently not possible, but we do plan to support this in the future.

### Can I utilize the Polars GPU engine in Polars Cloud?

Yes! Simply start a compute instance with a supported GPU and pass `engine="gpu"` to your `spawn_query` call.
