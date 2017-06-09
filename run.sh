#!/bin/bash

crontab -l | { cat; echo "0 * * * * python3 ~/workspace/dontIP/ipupdater.py http://dontpad.com/ipghiggi"; } | crontab -
