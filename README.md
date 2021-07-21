# starter

An example Flask-based web application, deployable to Kubernetes with all the
essentials.

## Getting started - locally

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
to use the `make console` target:

```bash
make build
make console

# Then from inside the container's shell...
flask 