#!/bin/sh
set -e
umask 022
cfg=/cfg
chmod -R a+rX /cfg

yum --quiet --assumeyes install $(cat /cfg/yum-install.list)

sh /cfg/install-root.sh

exec_user=vagrant
useradd --create-home $exec_user
su --login $exec_user --command="sh /cfg/install-exec-user.sh"