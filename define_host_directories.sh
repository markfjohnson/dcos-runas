#!/usr/bin/env bash
sudo mkdir -p /data/org_super_secret
sudo chmod 700 /data/org_super_secret

sudo mkdir -p /data/my_data
sudo chmod 770 /data/my_data
sudo chown dcosuser:dcos /data/my_data
