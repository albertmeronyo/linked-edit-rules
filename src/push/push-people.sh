#!/usr/bin/bash

CWD=$(pwd)
cd /opt/virtuoso7/bin
./isql -U dba -P $1 -S 3111 < $CWD/push-people.sql
