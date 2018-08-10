#!/bin/bash
apt-get -y update&&echo -e "\e[32m######update#####OK#######\e[m\n"

apt-get -y upgrade&&echo -e "\e[32m#####upgrade####OK#######\e[m\n"

apt-get -y dist-upgrade&&echo -e "\e[32m######dist-upgrade######OK######\e[m\n"

apt-get -f install&&echo -e "\e[32m######fix-install######OK######\e[m\n"

apt-get -y autoclean&&echo -e "\e[32m######autoclean######OK######\e[m\n"

apt-get -y autoremove&&echo -e "\e[32m######automove######OK######\e[m\n"

apt-get check
echo -e "\e[32m######check######over########\e[m\n"
echo -e "\e[32m######over######over##########\e[m\n"
