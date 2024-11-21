# Getting started

## Prerequisites

- AWS account with certain minimum permissions
- ...

## Creating an account

## Setting up a workspace

## Authenticating with Polars Cloud



## Running a query

Now that we're authenticated, it's time to run a query on the Polars Cloud.
Let's say we have an existing Polars script 

```python
import polars as pl

df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 4, 5]})

lf = df.lazy().with_columns(pl.col("a").max().over("b").alias("c"))

result = lf.collect()
print(result)
```

