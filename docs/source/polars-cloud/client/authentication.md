# Authentication

Overview of the available authentication flows.

## Keycloak

We use [Keycloak](https://www.keycloak.org/) to take care of the heavy lifting for us.

## Authentication flows
We support two authentication flows in the client: the client credentials flow and the device authorization flow.

### Client credentials

The client credentials flow is intended for automated workflows. The user first needs to request a client ID and client secret in the admin dashboard. These credentials can then be provided while executing a Python program to get a Polars Cloud access token.

Auth0 documentation on this authentication flow can be found here.

The following should be kept in mind when using the client credentials flow:

- The credentials should usually be set as environment variables `POLARS_CLOUD_CLIENT_ID` and `POLARS_CLOUD_CLIENT_SECRET`.
- If no valid access token is available yet, the first Polars Cloud command (e.g. `start_server`) will automatically try to retrieve a new access token. This token will be cached in memory for subsequent commands.
- It is also possible to trigger this authentication flow explicitly by using the `authenticate` function. This can be useful if you want more control over when the authentication request happens and where to store the access token.

#### Example

The following example showcases the client credentials flow. Note that this code is just for demonstration purposes: normally, your environment variables will be set externally (e.g. through a `.env` file) and authentication is handled automatically when using Polars Cloud commands.

```python
import polars_cloud as plc
import os
​
# Set the client credentials as environment variables
os.environ["POLARS_CLOUD_CLIENT_ID"] = "<INSERT CLIENT ID>"
os.environ["POLARS_CLOUD_CLIENT_SECRET"] = "<INSERT CLIENT SECRET>"
​
# Request an access token
token = plc.authenticate()
print(token)
```

### Device authorization

The device authorization flow is intended for interactive workflows, e.g. in Notebooks. The user logs in through the browser with their Polars Cloud account, and recieves an access token which is stored on disk.

Auth0 documentation on this authentication flow can be found [here](https://auth0.com/docs/get-started/authentication-and-authorization-flow/device-authorization-flow).

The following should be kept in mind when using the device authorization flow:

- The flow is triggered manually by using the `login` function. This will open a web browser in which the user completes the authenticaton process.
- By default, the access token is stored to disk at `~/.polars/cloud_access_token`. This behavior can be influenced by tweaking the parameters of the login function or setting the `POLARS_CLOUD_ACCESS_TOKEN_PATH` environment variable.
- If storing the token to disk is not an option, it is also possible to get the token as a string by calling `login(return_token=True)` and then setting the environment variable `POLARS_CLOUD_ACCESS_TOKEN`.

#### Example

The following example showcases the device authorization flow. After running this code and completing the login process, an access token should be saved to `~/.polars/cloud_access_token`.

```python
import polars_cloud as plc
​
plc.login()
```
