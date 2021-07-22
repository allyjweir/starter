# starter

An example Flask-based web application, deployable to Kubernetes with all the
essentials.

## Problem Definition

Develop a webservice and implement the following methods:

1. `/add`
    - It will take two numbers and add them together.
    - Return the result of adding them.
2. `/substract`
    - It will take two real numbers and return the result of subtracting them.
3. `/division`
    - Divide two numbers, return the result.
4. `/random`
    - Optional argument Count.
    - It will return by default 10 random numbers if Count provided, return the amount of random numbers requested.
5. `/metrics`
    - Provide prometheus metrics that you see fit.
6. `/readiness`
    - 200 if service is ready to take requests.
7. `/liveness`
    - 200 if the service is alive.

Also:

- Include unit tests
- Dockerize the above webservice.
- Employ the best practices you are aware of to create a good container image.
- Create Kubernetes manifests to deploy this web service into Kubernetes.
  - Use the nginx ingress class.

## Getting Started - Locally

A `Makefile` is provided with various utility targets to help you get going. A
good place to start is to try running the tests:

```bash
# From root of project...
make build
# Output from docker build here...
make test
# Test output here...
```

While developing the application locally, the easiest way to run the server is
to use the `make run` target:

```bash
make build
make run
```

This will start the application in an auto-reload mode where if you make any
changes to your local files, the server will automatically restart.
