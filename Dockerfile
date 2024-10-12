FROM ubuntu:22.04

# Basic setup
RUN apt-get update
RUN apt-get install -y wget tar xz-utils python3

# Install and configure Blender
RUN apt-get install -y libx11-6 xorg
RUN mkdir /usr/local/blender/
RUN wget https://download.blender.org/release/Blender3.6/blender-3.6.15-linux-x64.tar.xz -O blender.tar.xz
RUN tar xf blender.tar.xz && mv blender-3.6.15-linux-x64 blender
RUN rm blender.tar.xz
RUN mv blender /usr/local
RUN ln -s /usr/local/blender/blender /usr/local/bin/blender

# Prepare workspace
RUN mkdir app && mkdir app/assets && mkdir app/scripts
COPY ./scripts /app/scripts
WORKDIR /app

RUN ls -la /app/scripts

# Start container
ENTRYPOINT ["blender"]
CMD ["-b", "-noaudio", "--python-exit-code", "1", "-P", "/app/scripts/main.py", "--", "--input", "/app/assets"]
