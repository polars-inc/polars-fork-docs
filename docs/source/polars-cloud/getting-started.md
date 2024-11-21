# Getting started

This guide will help you get up-and-running with Polars Cloud in no time! Note that the first part
of this guide is targeted at 'admin' users and includes setting up an account and workspace. If your
organization has already set this up for you, you can start at the
[authenticating](#authenticating-with-polars-cloud) section.

!!! Tip

    This step-by-step guide assumes you're starting from scratch.
    If you have already completed some of these steps before,
    the examples may need to be adjusted slightly to make them work.

## Prerequisites

In order to use Polars Cloud, you obviously need access to the cloud! At this moment, Polars only
supports Amazon Web Services (AWS) as a cloud provider. The following are required:

- An AWS account with certain minimum permissions (see [workspaces](./workspaces.md) for details).
- An AWS S3 bucket. Polars Cloud queries always write their result to an S3 bucket.

## Creating an account

(Some instructions on which URL to go / what buttons to click)

## Setting up a workspace

(Some instructions on which URL to go to / what buttons to click)

## Authenticating with Polars Cloud



```python
import polars_cloud as plc

plc.login()
```

For additional details on authentication, check out the [authentication](./client/authentication.md) section.

## Defining a compute context

Before we can run a query on Polars Cloud, we need to specify which type of compute to use. This is
done using the `ComputeContext` class.

```python
import polars_cloud as plc

compute = plc.ComputeContext(instance_type="t2.micro")
```

It's possible to set the context as the default for this workspace. That way, we don't have to
define it next time.

```
compute.set_default()
```

## Running a query

Now that we're authenticated and have specified the type of compute to use, it's time to run a query
on the Polars Cloud.

Let's say we have the following Polars script that we want to run on Polars Cloud instead of
locally:

```python
import polars as pl

df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 4, 5]})

lf = df.lazy().with_columns(pl.col("a").max().over("b").alias("c"))

result = lf.collect()
print(result)
```

To run this query on Polars Cloud, we replace the `collect` call with Polars Cloud functionality:

```python
import polars as pl
import polars_cloud as plc

df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 4, 5]})

lf = df.lazy().with_columns(pl.col("a").max().over("b").alias("c"))

uri = "s3://my-bucket/result.parquet"
query = plc.spawn_query(lf, uri=uri)
result = query.await_result()
print(result)
```

Note that we have changed the `collect` call into two new calls:

- `spawn_query` starts a new compute cluster using the defaults we just defined, then sends the
  query to Polars Cloud to be executed. The result is written to the given location on S3.
- `await_result` polls the query until it has finished running and returns a small number of rows of
  the result.

If we want to get the full query output, we can read it from S3:

```
result = pl.read_parquet(uri)
print(result)
```

The compute cluster started for this query will automatically shut down after the query is complete.
However, the query result data on your S3 bucket will persist, so make sure to delete it if you do
not want to incur any additional fees.

For more examples and advanced usage, check out the [Client](./client/) section.
