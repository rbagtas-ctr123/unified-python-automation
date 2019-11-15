#!/bin/bash

echo "BEGINNING SAUCE CONNECT SETUP"
# Grab Latest Version
SAUCE_CONNECT_VERSION=$(curl --silent https://wiki.saucelabs.com/display/DOCS/Sauce+Connect+Proxy+Change+Logs \
  | grep -Eo "Sauce+Connect+Proxy+Version+[0-9].[0-9].[0-9]+" \
  | sed -n "1p" \
  | grep -Eo "[0-9].[0-9].[0-9]+")
# Download and Unzip
export SAUCE_CONNECT_VERSION
if [[ "$OSTYPE" == "linux-gnu" ]]; then
        wget -N https://saucelabs.com/downloads/sc-${SAUCE_CONNECT_VERSION}-linux.tar.gz
        tar -xvzf sc-${SAUCE_CONNECT_VERSION}-linux.tar.gz
        mv sc-${SAUCE_CONNECT_VERSION}-linux sauce_connect
        echo "SAUCE CONNECT DOWNLOAD COMPLETE"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        curl -O https://saucelabs.com/downloads/sc-${SAUCE_CONNECT_VERSION}-osx.zip
        tar -xvzf sc-${SAUCE_CONNECT_VERSION}-osx.zip
        mv sc-${SAUCE_CONNECT_VERSION}-osx sauce_connect
        echo "SAUCE CONNECT DOWNLOAD COMPLETE"
else
  echo "ERROR: Incompatiable OS Type"
  echo "Download of Sauce Connect will not proceed!"
fi
