#!/bin/sh
set -e
curl –s -L https://raw.githubusercontent.com/biviosoftware/home-env/master/install.sh | bash
. ~/.bashrc
b_install_pyenv 2
curl -s -L https://raw.githubusercontent.com/radiasoft/foss-mirror/master/install-as-user.sh | bash
cd ~/src/biviosoftware
git clone -q https://github.com/biviosoftware/pybivio
cd pybivio
pip install -e .
mkdir -p ~/src/radiasoft
cd ~/src/radiasoft
git clone -q https://github.com/radiasoft/radtrack
cd radtrack
pip install -e .
