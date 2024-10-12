# Docker Blender USDZ Exporter

## Overview

This project allows to convert GLB files to USDZ with Docker and Blender.
Using this setup, any other package or library (eg. USD) is not required.

## Requirements

- Docker

## How to use

1. Run with Docker:

Copy your GLB files to a folder and then run these commands in the terminal:

```bash
docker build --progress plain -t b3d-usdz-convert .
docker run -it -v /path/to/glbs-folder:/app/assets b3d-usdz-convert
```

2. Run `export_usdz.sh` script:

```bash
bash export_usdz.sh /path/to/glbs-folder
```
