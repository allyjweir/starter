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

## Deployment - Minikube

This application was developed to deploy against minikube with its nginx ingress
addon configured. Please see the `make deploy_to_minikube` target and associated
script for how this deployment works.

### Pre-requisites

1. Have [`kapp`](https://carvel.dev/kapp/) installed. This is used to deploy the
application's manifest to the cluster, grouping its resources.
2. Have built and published the Dockerfile to Docker Hub. (Hint: use
`make publish_image`)
3. Change out the `image` field in the Deployment's pod spec to match where you
pushed your image

## Notes on the Kubernetes Manifest

Typically I would use a Helm chart here but for this small example, I went for
a simpler bare YAML approach with `kapp` to take care of the application
management side of things. In the past I have also used
[ArgoCD](<https://argoproj.github.io/argo-cd/>) successfully to complete this
responsiblity of deployment lifecycle management in a GitOps pattern.

When it comes to the task of templating itself, an alternative I have been
exploring recently would be to use [`ytt`](<https://carvel.dev/ytt/>) to
template and patch the manifest as required before then using `kapp` or ArgoCD
to deploy.
