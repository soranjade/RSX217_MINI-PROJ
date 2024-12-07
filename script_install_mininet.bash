#!/bin/bash

# Remove old mininet
sudo apt remove -y mininet

# Get mininet src
git clone https://github.com/mininet/mininet
cd mininet
git fetch
git checkout -b mininet-2.3.1b4
# Launch install with PY3
PYTHON=python3 util/install.sh -a
