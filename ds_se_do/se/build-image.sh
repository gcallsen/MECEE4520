#!/bin/bash

cd ..

echo "Building Python egg ..."
python setup.py sdist

PKG_FILENAME=`ls -t ./dist | head -n1`

cp ./dist/$PKG_FILENAME ./se/$PKG_FILENAME

# Build the docker image
echo "Building Docker image ..."

cd se

docker build\
  --build-arg PKG_FILENAME=$PKG_FILENAME\
  -t mecee4520\
  .

echo "Cleaning up ..."
rm ./$PKG_FILENAME

echo "Fin."