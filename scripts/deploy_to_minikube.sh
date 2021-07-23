#!/bin/bash

set -eu

if ! kapp --version; then
    echo "kapp is used to deploy to minikube."
    echo "Please install here: https://carvel.dev/kapp/"
    exit 1
fi

minikube addons enable ingress

kapp deploy --yes --app starter-app --file deployment/manifest.yaml

echo "If you haven't already, make sure to configure your minikube nginx ingress in /etc/hosts as specified here: https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/#create-an-ingress-resource"