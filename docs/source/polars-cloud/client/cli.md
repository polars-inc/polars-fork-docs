# Command line interface

Part of the Python SDK is also available through a command line interface (CLI). This may be useful
when interacting with Polars Cloud programmatically, e.g. in a CI/CD pipeline.

## Installation

The CLI is available automatically after installing the Python package.
It can be called with the `plc` command:

```bash
pip install polars-cloud
plc --version
```

## Usage

The CLI offers the same functionality as the Python SDK.
Below are a few examples of CLI usage.

Log in through the browser:

```
plc login
```

List all available workspaces:

```
plc workspace list
```

Start a compute cluster:

```
plc compute start --instance-type t2.micro --workspace <YOUR-WORKSPACE_ID>
```

## Limitations

Submitting a new query or retrieving the results of a query are not available in the CLI. These
actions involve sending or receiving Python objects, so doing this over the CLI is not sensible.
Please use the Python SDK for these actions instead.
