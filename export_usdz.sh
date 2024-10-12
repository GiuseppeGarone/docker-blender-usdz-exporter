#!/bin/bash
GLB_FOLDER="$1"
docker build --progress plain -t b3d-usdz-convert .
docker run -it -v $GLB_FOLDER:/app/assets b3d-usdz-convert
