#!/bin/bash
apt-get -y update&&apt-get -y upgrade&&apt-get -y dist-upgrade&&apt-get -f install&&apt-get -y autoclean&&apt-get -y autoremove&&apt-get check
echo ""
echo -e "\e[32m######over######over######\e[m\n"

