#!/bin/bash

if [[ $(git diff --stat) != '' ]]; then
  echo 'Working directory is not clean. Please commit/stash changes before publish the latest image to Docker Hub.'
  exit 1
fi

make build

new_tag="allyjweir/starter:$(git rev-parse --short HEAD)"
docker tag starter:local_dev $new_tag
docker push $new_tag
echo "Successfully published $new_tag to Docker Hub."