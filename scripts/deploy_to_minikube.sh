#!/bin/bash

set -eu

if [ "$(kubectl config current-context)" != "minikube" ]; then
    echo "This script expects minikube to be running and set as the current kubectl context."
    exit 1
fi

echo "Ensuring minikube's ingress addon is configured"
echo "======"
minikube addons enable ingress

echo
echo "Verifying kapp is installed"
echo "======"
if ! kapp --version; then
    echo "kapp is used to deploy to minikube."
    echo "Please install here: https://carvel.dev/kapp/"
    exit 1
fi

echo
echo "Deploying app via kapp"
echo "======"
kapp deploy --yes --app starter-app --file deployment/manifest.yaml

echo
echo "NOTES"
echo "======"
echo "1) Make sure to configure your minikube nginx ingress in /etc/hosts as specified here: https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/#create-an-ingress-resource"