# chaos-service
chaos-service is a CLI that set up a mock service that will emulate failures (such as internal server error, connection refused, etc.) for chaos testing purposes.

To install, just type:
    
    pip3 install .

To execute the CLI, type:

    chaos-service --help

When you start the service (for example by typing `chaos-service chaos --chance-of-sucess 90`) it will create an API with 2 endpoints:

```
GET localhost:8080/v1/chaos/get
POST localhost:8080/v1/chaos/post
```

These API's will throw errors following what you configured via CLI.